from OpenAi import Embedding
from OpenAi.Embedding import *
from Models.Models import *
from Scrape.Scrape import *
from VectorDataBase.VectorDataBase import *
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from fastapi import File, UploadFile
from OpenAi.OpenAi import *
import tiktoken
import shutil

class Logic:
    def __init__(self):
        pass

    def url_scrape(self, scrape_request_body: URLScrapeRequestBody):
        documents = Scrape().scrape_urls(scrape_request_body.urls)
        self.embedding_documents(documents=documents)
        return ScrapeResponseBody(status="in progress")

    def document_scrape(self, files: List[UploadFile]):
        for file in files:
            path = f'files/{file.filename}'
            with open(path, 'w+b') as buffer:
                shutil.copyfileobj(file.file, buffer)
            # if file.content_type == 'application/pdf':
            documents = Scrape().scrape_document(path)
            self.embedding_documents(documents=documents)
            print(path)

    def embedding_documents(self, documents: Document):
        for doc in documents:
            # Milvus db max varchar length is 65535
            if len(doc.page_content) > 65535:
                return "error"
        embeddings = Embedding.get_embeddings()
        VectorDataBase(embeddings=embeddings).store_embeddings_with_azure(documents=documents)

    def ask(self, question: str):
        embeddings = Embedding.get_embeddings()
        docs = VectorDataBase(embeddings=embeddings).similarity_search(question)
        if len(docs) < 1:
            return AskResponseBody(answer="error")

        # OpenAIChat currently only supports single prompt
        # we need to joint related documents together
        document = Document(page_content="")
        documentSources = ""
        for doc in docs:
            document.page_content += doc.page_content + ","
            documentSources += doc.metadata['source'] + ","
        document.metadata = {"source": documentSources}

        tokenizer = tiktoken.get_encoding("cl100k_base")
        documentTokens = tokenizer.encode(document.page_content)

        # gpt-3.5-turbo maximum token limit is 4,096 tokens
        # 200 is langchain prompt tokens
        if len(documentTokens) <= 4096 - 200:
            documents = [document]
        else:
            documents = [docs[0]]

        openAi = OpenAi().get_openAi()
        chain = load_qa_with_sources_chain(openAi, chain_type="map_reduce",
                                           return_intermediate_steps=True)
        result = chain({"input_documents": documents, "question": question}, return_only_outputs=True)
        return AskResponseBody(answer=result["output_text"])


if __name__ == "__main__":
    question = "test"
    logic = Logic()
    # answer = logic.ask(question="what?")
    urls = [
        "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-february-8-2023"
    ]
    s = URLScrapeRequestBody(urls=urls)
    answer = logic.scrape(scrapeRequestBody=s)
    print(answer)

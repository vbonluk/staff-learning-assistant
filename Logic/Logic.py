from OpenAi import Embedding
from OpenAi.Embedding import *
from Models.Models import *
from Scrape.Scrape import *
from VectorDataBase.VectorDataBase import *
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from OpenAi.OpenAi import *


class Logic:
    def __init__(self):
        pass

    def url_scrape(self, scrape_request_body: URLScrapeRequestBody):
        documents = Scrape().scrape_urls(scrape_request_body.urls)
        for doc in documents:
            # Milvus db max varchar length is 65535
            if len(doc.page_content) > 65535:
                return "error"
        embeddings = Embedding.get_embeddings()
        VectorDataBase(embeddings=embeddings).store_embeddings_with_azure(documents=documents)
        return ScrapeResponseBody(status="in progress")

    def ask(self, question: str):
        embeddings = Embedding.get_embeddings()
        docs = VectorDataBase(embeddings=embeddings).similarity_search(question)
        # te
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

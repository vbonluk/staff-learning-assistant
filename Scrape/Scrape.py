from langchain.document_loaders import SeleniumURLLoader
from langchain.text_splitter import CharacterTextSplitter
from typing import List


class Scrape:
    def __init__(self):
        pass

    def normalize_text(self, text):
        # remove all instances of multiple spaces
        text = text.replace("..", ".")
        text = text.replace(". .", ".")
        text = text.replace("\n", "")
        text = text.strip()
        return text

    def scrape_urls(self, urls: List[str]):
        loader = SeleniumURLLoader(urls=urls)
        documents = loader.load()
        # page_content = documents[0].page_content
        # content = page_content
        # text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        #     chunk_size=1000, chunk_overlap=0
        # )
        # texts = text_splitter.split_text(content)

        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000,
            chunk_overlap=0,
        )
        docs = text_splitter.split_documents(documents)

        return docs


if __name__ == "__main__":
    question = "test"
    scrape = Scrape()
    urls = [
        "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-february-8-2023"
    ]
    result = scrape.scrapeUrls(urls)
    print(result)
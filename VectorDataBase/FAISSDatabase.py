from typing import List
from langchain.vectorstores import FAISS
from langchain.vectorstores.base import Embeddings
from langchain.vectorstores.base import Document


class FAISSDatabase:
    def __init__(self, embeddings: Embeddings):
        self.embeddings = embeddings

    def store_embeddings_with_azure(self, documents: List[Document]):
        # will using self.embeddings to embedding texts
        # then store texts to vector db
        # will create vector db collection and field and index
        # default index is HNSW

        # because azure openai only allow embedding one text every rpc call
        # so we need to for loop
        # ref: https://github.com/hwchase17/langchain/issues/4575
        for doc in documents:
            faissDB = FAISS.from_documents([doc], self.embeddings)
            faissDB.save_local("faiss_index")

    def similarity_search(self, query: str):
        # will using self.embeddings to embedding query
        # then similarity_search
        faissDB = FAISS.load_local("faiss_index", self.embeddings)
        return faissDB.similarity_search(query=query)


if __name__ == "__main__":
    pass

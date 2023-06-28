from typing import List
from langchain.vectorstores import Milvus
from langchain.vectorstores.base import Embeddings
from langchain.vectorstores.base import Document

MILVUS_HOST = "localhost"
MILVUS_PORT = "19530"
COLLECTON_NAME = "LangChainCollection"


class VectorDataBase:
    def __init__(self, embeddings: Embeddings):
        self.embeddings = embeddings
        self.vector_db = Milvus(
            embedding_function=embeddings,
            collection_name=COLLECTON_NAME,
            connection_args={
                "host": MILVUS_HOST,
                "port": MILVUS_PORT
            },

        )

    def get_vector_db(self):
        return self.vector_db

    def store_embeddings(self, documents: List[Document]):
        # will using self.embeddings to embedding texts
        # then store texts to vector db
        # will create vector db collection and field and index
        # default index is HNSW

        # self.vector_db.from_documents(
        #     documents=documents,
        #     embedding=self.embeddings
        # )
        self.vector_db.add_documents(documents)

    def store_embeddings_with_azure(self, documents: List[Document]):
        # will using self.embeddings to embedding texts
        # then store texts to vector db
        # will create vector db collection and field and index
        # default index is HNSW

        # because azure openai only allow embedding one text every rpc call
        # so we need to for loop
        # ref: https://github.com/hwchase17/langchain/issues/4575
        for doc in documents:
            self.vector_db.add_documents([doc])
            # self.vector_db.from_documents(
            #     documents=[doc],
            #     embedding=self.embeddings
            # )

    def similarity_search(self, query: str):
        # will using self.embeddings to embedding query
        # then similarity_search
        return self.vector_db.similarity_search(query=query, k=3)


if __name__ == "__main__":
    pass

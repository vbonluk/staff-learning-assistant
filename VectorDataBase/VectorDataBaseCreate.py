from VectorDataBase.VectorDataBase import *
from OpenAi.Embedding import Embedding


class VectorDataBaseCreate:
    def __init__(self):
        embeddings = Embedding.get_embeddings()
        self.vector_db = VectorDataBase(embeddings=embeddings).get_vector_db()

    def create(self):
        self.vector_db.similarity_search()
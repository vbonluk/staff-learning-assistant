from langchain.embeddings import OpenAIEmbeddings


class Embedding:
    def __init__(self):
        pass

    @classmethod
    def get_embeddings(cls):
        return OpenAIEmbeddings(model='text-embedding-ada-002',
                                deployment="staff-learning-assistant-embedding-model-01")

    def embedding(self, text: str):
        openAI_embeddings = self.get_embeddings()
        embedding_result = openAI_embeddings.embed_query(text)
        return embedding_result


if __name__ == "__main__":
    embedding = Embedding()
    print(embedding.embedding("hello world"))

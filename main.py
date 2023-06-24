from langchain.llms import AzureOpenAI
from langchain.embeddings import OpenAIEmbeddings

llm = AzureOpenAI(
    deployment_name="staff-learning-assistant-model-01",
    model_name="gpt-35-turbo",
)

# result = llm("Tell me a joke")
# print(result)

embeddings = OpenAIEmbeddings(model='text-embedding-ada-002', deployment="staff-learning-assistant-embedding-model-01")

text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result)
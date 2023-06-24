from langchain.llms import AzureOpenAI


class OpenAi:
    def __init__(self):
        pass

    def get_openAi(self):
        return AzureOpenAI(
            engine="staff-learning-assistant-model-01",
            model_name="gpt-3.5-turbo"
        )


if __name__ == "__main__":
    pass

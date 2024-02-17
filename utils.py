import os
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import AzureChatOpenAI
from prompts import CHATGPT_PROMPT

from dotenv import load_dotenv
load_dotenv("credentials.env")

class ChatGPT:
    """Class for a ChatGPT clone"""

    name = "@chatgpt"
    description = "useful when the questions includes the term: @chatgpt.\n"
    
    def __init__(self):
        self.llm = AzureChatOpenAI(
                openai_api_key=os.environ['AZURE_OPENAI_API_KEY'],
                api_version=os.environ['AZURE_OPENAI_API_VERSION'],
                azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'],
                deployment_name=os.environ['AZURE_OPENAI_MODEL_NAME'],
                model_name=os.environ['AZURE_OPENAI_MODEL_NAME'],
                temperature=0
            )
        self.memory = ConversationBufferWindowMemory(memory_key="conversation_memory", return_messages=True, k=5)

    def _run(self, query: str) -> str:
        try:
            chatgpt_chain = LLMChain(
                llm=self.llm,
                prompt=CHATGPT_PROMPT,
                verbose=True,
                memory=self.memory
            )

            response = chatgpt_chain.run(query)

            return response
        except Exception as e:
            print(e)
            return "An error occurred while processing your request."

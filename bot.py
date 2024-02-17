import os
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from prompts import WELCOME_MESSAGE
from utils import ChatGPT


from dotenv import load_dotenv
load_dotenv("credentials.env")


class MyBot(ActivityHandler):
    def __init__(self):
        super(MyBot, self).__init__()
         
        # Create an instance of ChatGPT      
        self.chat_gpt = ChatGPT()  
        
        

    async def on_message_activity(self, turn_context: TurnContext):
        query = turn_context.activity.text
        response = await self._run(query)
        await turn_context.send_activity(response)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(WELCOME_MESSAGE)

    async def _run(self, query: str) -> str:
        # Call the _run method of ChatGPT instance
        return self.chat_gpt._run(query)
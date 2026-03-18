from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from agent.agent import create_agent

load_dotenv()

model = init_chat_model("claude-3-haiku-20240307", temperature=0)

agent = create_agent()

agent.invoke({"messages": [("user", "Can you predict the stock market price for AAPL for the next 30 days?")]})
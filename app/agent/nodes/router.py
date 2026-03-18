from pydantic import BaseModel, Field
from typing import Literal
from langchain_anthropic import ChatAnthropic
from app.agent.state import State

class RouteSelection(BaseModel):
    """Determins ther next step in the stock portfolio managment workflow based on user intent"""
    next_node: Literal["analyst_node", "prepare_trade_node", "reporter_node", "general_chat"]
    reasoning: str = Field(description="Explain your reasoning for the next step")

def router(state: State) -> str:
    """Router that decides which node to go to next based on user intent"""
    llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
    structured_llm = llm.with_structured_output(RouteSelection)

    system_prompt = (
        "You are a routing assistant for a stock portfolio manager. "
        "Classify the user's intent into: "
        "- analyst_node: For market research, stock suggestions, or 'should I' questions. "
        "- reporter_node: For checking profits, balance, or current holdings. "
        "- prepare_trade_node: For explicit requests to buy or place orders. "
        "- general_chat: for greetings or off-topic questions."
    )

    selection = structured_llm.invoke([{"role": "system", "content": system_prompt}] + state["messages"])
    
    return selection.next_node
from langgraph.graph import StateGraph, END
from app.agent.nodes.analyst_node import get_attr_analyst_node
from app.agent.nodes.reporter_node import get_attr_reporter_node
from app.agent.nodes.prepare_trade_node import get_attr_prepare_trade_node
from app.agent.nodes.router import router
from app.agent.state import State

def create_agent():
    builder = StateGraph(State)
    builder.add_node("analyst_node", get_attr_analyst_node())
    builder.add_node("reporter_node", get_attr_reporter_node())
    builder.add_node("prepare_trade_node", get_attr_prepare_trade_node())
    builder.set_conditional_entry_point(
        router,
        {
            "analyst_node": "analyst_node",
            "reporter_node": "reporter_node",
            "prepare_trade_node": "prepare_trade_node",
            "general_chat": END,
        }
    )

    # import PIL.Image
    # import io
    # png_data = graph.get_graph().draw_mermaid_png()
    # img = PIL.Image.open(io.BytesIO(png_data))
    # img.show()

    return builder.compile()
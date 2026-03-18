from agent.state import State

def get_attr_prepare_trade_node():
    """This is a factory function that returns a node that can be used in the graph"""

    def prepare_trade_node(state: State) -> State:
        print("--- PREPARING TRADE ---")
        return {"messages": ["I've set up the order for NVDA. Please confirm to execute."]}
    
    return prepare_trade_node
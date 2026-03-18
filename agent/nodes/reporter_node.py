from agent.state import State

def get_attr_reporter_node():
    """This is a factory function that returns a node that can be used in the graph"""

    def reporter_node(state: State) -> State:
        print("--- FETCHING PORTFOLIO ---")
        return {"messages": ["Your current portfolio is up 5% today. Total equity: $10,500."]}
    
    return reporter_node
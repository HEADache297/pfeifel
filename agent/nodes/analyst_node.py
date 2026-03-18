from agent.state import State

def get_attr_analyst_node():
    """This is a factory function that returns a node that can be used in the graph"""

    def analyst_node(state: State) -> State:
        print("--- ANALYZING MARKET ---")
        return {"messages": ["I've analyzed the tech sector. NVIDIA looks strong based on recent news."]}
    
    return analyst_node
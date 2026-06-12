from langgraph.graph import (
    StateGraph,
    END
)

from workflow.state import AgentState

from workflow.graph import (
    router_node,
    finance_node,
    customer_node,
    product_node,
    executive_node
)


def route(state):

    return state["agent"]


graph = StateGraph(
    AgentState
)

graph.add_node(
    "router",
    router_node
)

graph.add_node(
    "finance",
    finance_node
)

graph.add_node(
    "customer",
    customer_node
)

graph.add_node(
    "product",
    product_node
)

graph.add_node(
    "executive",
    executive_node
)

graph.set_entry_point(
    "router"
)

graph.add_conditional_edges(
    "router",
    route,
    {
        "finance": "finance",
        "customer": "customer",
        "product": "product",
        "executive": "executive"
    }
)

graph.add_edge(
    "finance",
    END
)

graph.add_edge(
    "customer",
    END
)

graph.add_edge(
    "product",
    END
)

graph.add_edge(
    "executive",
    END
)

app = graph.compile()
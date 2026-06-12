from workflow.router import route_question

from agents.finance_agent import finance_agent
from agents.customer_agent import customer_agent
from agents.product_agent import product_agent
from agents.executive_agent import executive_agent


def router_node(state):

    state["agent"] = route_question(
        state["question"]
    )

    return state


def finance_node(state):

    state["answer"] = finance_agent(
        state["question"]
    )

    return state


def customer_node(state):

    state["answer"] = customer_agent(
        state["question"]
    )

    return state


def product_node(state):

    state["answer"] = product_agent(
        state["question"]
    )

    return state


def executive_node(state):

    state["answer"] = executive_agent(
        state["question"]
    )

    return state
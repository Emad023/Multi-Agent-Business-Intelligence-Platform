from workflow.router import route_question

from agents.finance_agent import finance_agent
from agents.customer_agent import customer_agent
from agents.product_agent import product_agent
from agents.executive_agent import executive_agent


def supervisor(question):

    agent = route_question(question)

    print(f"\nSelected Agent: {agent}")

    if agent == "finance":
        return finance_agent(question)

    elif agent == "customer":
        return customer_agent(question)

    elif agent == "product":
        return product_agent(question)

    else:
        return executive_agent(question)
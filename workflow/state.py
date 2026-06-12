from typing import TypedDict


class AgentState(TypedDict):

    question: str

    agent: str

    answer: str
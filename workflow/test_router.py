from workflow.router import route_question

questions = [

    "What is our profit margin?",

    "Which customer segment generates the most revenue?",

    "What are our top products?",

    "Give me an executive summary"
]

for q in questions:

    print(
        f"Question: {q}"
    )

    print(
        f"Agent: {route_question(q)}"
    )

    print("-" * 50)
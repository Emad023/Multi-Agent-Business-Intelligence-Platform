from workflow.supervisor import supervisor

questions = [

    "What is our profit margin?",

    "Which customer segment generates the most revenue?",

    "What are our top products?",

    "Give me an executive summary"
]

for q in questions:

    print("\n" + "=" * 60)
    print("QUESTION:")
    print(q)

    result = supervisor(q)

    print("\nRESULT:")
    print(result)

    print("=" * 60)
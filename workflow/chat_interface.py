from workflow.supervisor import supervisor

print("=" * 60)
print("Multi-Agent Business Intelligence Platform")
print("=" * 60)

while True:

    question = input("\nAsk a business question: ")

    if question.lower() in ["exit", "quit"]:

        print("\nGoodbye!")
        break

    result = supervisor(question)

    print("\n")
    print("=" * 60)
    print("RESPONSE")
    print("=" * 60)

    print(result)
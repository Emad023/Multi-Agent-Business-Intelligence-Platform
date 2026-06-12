from workflow.langgraph_orchestrator import app

result = app.invoke(
    {
        "question":
        "What is our profit margin?"
    }
)

print()

print(result["answer"])
from services.executive_service import (
    generate_executive_summary
)

from vector_db.rag_pipeline import (
    retrieve_context
)

def executive_agent(question):

    summary = generate_executive_summary()

    context = retrieve_context(question)

    return {
        "question": question,
        "summary": summary,
        "context": context
    }


if __name__ == "__main__":

    result = executive_agent(
        "Give me an executive overview"
    )

    print(result["summary"])

    print("\n")

    print(result["context"])
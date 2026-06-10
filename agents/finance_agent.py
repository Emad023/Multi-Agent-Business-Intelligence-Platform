from services.finance_service import (
    get_financial_summary
)

from vector_db.rag_pipeline import (
    retrieve_context
)


def finance_agent(question):

    finance_data = get_financial_summary()

    context = retrieve_context(question)

    return {
        "question": question,
        "finance_data": finance_data,
        "context": context
    }


if __name__ == "__main__":

    result = finance_agent(
        "What is our profit margin?"
    )

    print(result["finance_data"])

    print("\n")

    print(result["context"])
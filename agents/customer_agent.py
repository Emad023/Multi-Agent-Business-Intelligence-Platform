from services.customer_service import (
    get_customer_segments
)

from vector_db.rag_pipeline import (
    retrieve_context
)

def customer_agent(question):

    customer_data = get_customer_segments()

    context = retrieve_context(question)

    return {
        "question": question,
        "customer_data": customer_data,
        "context": context
    }


if __name__ == "__main__":

    result = customer_agent(
        "Which customer segment generates the most revenue?"
    )

    print(result["customer_data"])

    print("\n")

    print(result["context"])
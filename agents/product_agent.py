from services.product_service import (
    get_top_products
)

from vector_db.rag_pipeline import (
    retrieve_context
)

def product_agent(question):

    product_data = get_top_products()

    context = retrieve_context(question)

    return {
        "question": question,
        "product_data": product_data,
        "context": context
    }


if __name__ == "__main__":

    result = product_agent(
        "What are our top products?"
    )

    print(result["product_data"])

    print("\n")

    print(result["context"])
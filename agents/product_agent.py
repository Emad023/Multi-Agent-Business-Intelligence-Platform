from llm.business_analyst import generate_business_answer
from services.product_service import get_top_products
from vector_db.rag_pipeline import retrieve_context


def product_agent(question):

    df = get_top_products()

    context = retrieve_context(question)

    answer = generate_business_answer(
        question=question,
        context=context,
        data=df.to_string()
    )

    return answer
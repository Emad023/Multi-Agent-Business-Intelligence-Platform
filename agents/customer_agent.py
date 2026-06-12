from llm.business_analyst import generate_business_answer
from services.customer_service import get_customer_segments
from vector_db.rag_pipeline import retrieve_context


def customer_agent(question):

    df = get_customer_segments()

    context = retrieve_context(question)

    answer = generate_business_answer(
        question=question,
        context=context,
        data=df.to_string()
    )

    return answer


if __name__ == "__main__":

    print(
        customer_agent(
            "Which customer segment generates the most revenue?"
        )
    )
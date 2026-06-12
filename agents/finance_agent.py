from services.finance_service import (
    get_financial_summary
)

from vector_db.rag_pipeline import (
    retrieve_context
)

from llm.business_analyst import (
    generate_business_answer
)


def finance_agent(question):

    finance = get_financial_summary()

    context = retrieve_context(
        question
    )

    data = {
        "total_revenue": float(finance["total_revenue"].iloc[0]),
        "total_profit": float(finance["total_profit"].iloc[0]),
        "profit_margin": float(finance["profit_margin"].iloc[0])
    }

    answer = generate_business_answer(
        question=question,
        context=context,
        data=data
    )

    return answer


if __name__ == "__main__":

    print(
        finance_agent(
            "What is our profit margin?"
        )
    )
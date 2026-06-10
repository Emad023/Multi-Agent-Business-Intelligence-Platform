from services.finance_service import get_financial_summary
from vector_db.rag_pipeline import retrieve_context


def finance_agent(question):

    finance = get_financial_summary()

    revenue = finance["total_revenue"].iloc[0]
    profit = finance["total_profit"].iloc[0]
    margin = finance["profit_margin"].iloc[0]

    context = retrieve_context(question)

    response = f"""
Financial Summary

Revenue: ${revenue:,.2f}

Profit: ${profit:,.2f}

Profit Margin: {margin:.2f}%

Business Context:
Profit margin is calculated as Profit ÷ Revenue.

The company generated strong revenue while maintaining a profit margin of {margin:.2f}%.
"""

    return response


if __name__ == "__main__":

    print(
        finance_agent(
            "What is our profit margin?"
        )
    )
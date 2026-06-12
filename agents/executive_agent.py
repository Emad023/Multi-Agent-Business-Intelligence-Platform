from llm.business_analyst import generate_business_answer
from services.executive_service import generate_executive_summary


def executive_agent(question):

    summary = generate_executive_summary()

    finance = summary["finance"]
    customers = summary["customers"]
    products = summary["products"]

    revenue = finance["total_revenue"].iloc[0]
    profit = finance["total_profit"].iloc[0]
    margin = finance["profit_margin"].iloc[0]

    top_segment = customers.iloc[0]["segment"]

    top_product = products.iloc[0]["product_name"]

    data = f"""
Revenue: ${revenue:,.2f}

Profit: ${profit:,.2f}

Profit Margin: {margin:.2f}%

Top Customer Segment:
{top_segment}

Top Revenue Product:
{top_product}
"""

    answer = generate_business_answer(
    question="""
Act as a Chief Business Officer.

Generate an executive summary based ONLY on the provided business data.

Requirements:
- Write a short executive overview paragraph.
- Mention revenue, profit, and profit margin.
- Mention the top customer segment.
- Mention the top revenue product.
- Provide 3-4 insights strictly supported by the data.
- Do not suggest partnerships, acquisitions, or new products unless supported by the data.
- Use professional executive language.
- Keep the response under 150 words.

Format:

Executive Summary

<paragraph>

Key Insights:
- Insight 1
- Insight 2
- Insight 3
- Insight 4
""",
    context="",
    data=data
)

    return answer
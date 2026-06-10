from services.executive_service import generate_executive_summary
from vector_db.rag_pipeline import retrieve_context


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

    response = f"""
Executive Summary

Revenue:
${revenue:,.2f}

Profit:
${profit:,.2f}

Profit Margin:
{margin:.2f}%

Top Customer Segment:
{top_segment}

Top Product:
{top_product}

Overall business performance remains positive with a healthy profit margin and strong contribution from the leading customer segment and product.
"""

    return response
from services.customer_service import get_customer_segments
from vector_db.rag_pipeline import retrieve_context


def customer_agent(question):

    df = get_customer_segments()

    top_segment = df.iloc[0]

    context = retrieve_context(question)

    response = f"""
Customer Segment Analysis

Top Segment:
{top_segment['segment']}

Customers:
{top_segment['customers']}

Revenue:
${top_segment['revenue']:,.2f}

This segment currently generates the highest revenue contribution.
"""

    return response
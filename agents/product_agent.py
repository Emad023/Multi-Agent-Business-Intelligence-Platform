from services.product_service import get_top_products
from vector_db.rag_pipeline import retrieve_context


def product_agent(question):

    products = get_top_products()

    top_product = products.iloc[0]

    context = retrieve_context(question)

    response = f"""
Top Product Analysis

Top Product:
{top_product['product_name']}

Revenue:
${top_product['revenue']:,.2f}

This is currently the highest revenue-generating product.
"""

    return response
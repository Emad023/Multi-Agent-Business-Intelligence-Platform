from services.finance_service import (
    get_financial_summary
)

from services.customer_service import (
    get_customer_segments
)

from services.product_service import (
    get_top_products
)


def generate_executive_summary():

    finance = get_financial_summary()

    customers = get_customer_segments()

    products = get_top_products()

    return {
        "finance": finance,
        "customers": customers,
        "products": products
    }
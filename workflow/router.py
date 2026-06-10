def route_question(question):

    question = question.lower()

    # Customer Questions
    if any(
        word in question
        for word in [
            "customer",
            "customers",
            "segment",
            "segments"
        ]
    ):
        return "customer"

    # Product Questions
    elif any(
        word in question
        for word in [
            "product",
            "products",
            "item",
            "items"
        ]
    ):
        return "product"

    # Finance Questions
    elif any(
        word in question
        for word in [
            "profit",
            "margin",
            "revenue",
            "finance",
            "sales"
        ]
    ):
        return "finance"

    return "executive"
from vector_db.qdrant_manager import (
    client,
    model
)

def retrieve_context(query):

    query_vector = model.encode(
        query
    ).tolist()

    results = client.query_points(
        collection_name="business_kb",
        query=query_vector,
        limit=3
    )

    contexts = []

    for point in results.points:

        contexts.append(
            point.payload["content"]
        )

    return "\n\n".join(contexts)


if __name__ == "__main__":

    question = "How is profit margin calculated?"

    context = retrieve_context(
        question
    )

    print("\nQUESTION:")
    print(question)

    print("\nRETRIEVED CONTEXT:")
    print(context)

    client.close()
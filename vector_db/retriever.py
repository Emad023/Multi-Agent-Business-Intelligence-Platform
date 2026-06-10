from vector_db.qdrant_manager import (
    client,
    model
)

query = "How is profit margin calculated?"

query_vector = model.encode(query).tolist()

results = client.query_points(
    collection_name="business_kb",
    query=query_vector,
    limit=3
)

for point in results.points:

    print("\n")
    print(point.payload["file"])

    print("-" * 50)

    print(point.payload["content"][:300])

client.close()
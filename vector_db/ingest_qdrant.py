from pathlib import Path

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from vector_db.qdrant_manager import (
    client,
    model
)

# Create collection
client.recreate_collection(
    collection_name="business_kb",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

# Load docs
docs = []

kb_path = Path("knowledge_base")

for file in kb_path.rglob("*.md"):

    with open(file, "r", encoding="utf-8") as f:

        content = f.read()

    docs.append(
        {
            "file": str(file),
            "content": content
        }
    )

# Insert docs
points = []

for idx, doc in enumerate(docs):

    embedding = model.encode(
        doc["content"]
    ).tolist()

    points.append(
        PointStruct(
            id=idx,
            vector=embedding,
            payload=doc
        )
    )

client.upsert(
    collection_name="business_kb",
    points=points
)

print(
    f"Inserted {len(points)} documents"
)
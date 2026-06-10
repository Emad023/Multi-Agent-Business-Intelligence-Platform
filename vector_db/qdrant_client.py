from qdrant_client import QdrantClient

client = QdrantClient(path="vector_db/qdrant_data")

print("Qdrant initialized")
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(
    path="vector_db/qdrant_data"
)

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
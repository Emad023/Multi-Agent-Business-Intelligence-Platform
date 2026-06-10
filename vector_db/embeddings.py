from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

text = "Revenue is calculated from sales."

embedding = model.encode(text)

print("Embedding dimension:", len(embedding))
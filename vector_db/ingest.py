from pathlib import Path

docs = []

kb_path = Path("knowledge_base")

for file in kb_path.rglob("*.md"):

    with open(file, "r", encoding="utf-8") as f:

        content = f.read()

    docs.append({
        "file": str(file),
        "content": content
    })

print("Documents loaded:", len(docs))

for doc in docs:
    print(doc["file"])
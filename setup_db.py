from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer

# 1. Connect to local Qdrant
client = QdrantClient("localhost", port=6333)

# 2. Load your exact model
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Create the collection (Size 384 for MiniLM, Cosine for similarity)
print("Creating 'knowledge' collection...")
client.recreate_collection(
    collection_name="knowledge",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

# 4. Create a test document
text = "Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management."
print(f"Embedding text: '{text}'")
vector = model.encode(text).tolist()

# 5. Insert it into Qdrant
print("Inserting document into database...")
client.upsert(
    collection_name="knowledge",
    points=[
        PointStruct(
            id=1,
            vector=vector,
            payload={"text": text}
        )
    ]
)
print("✅ Success! Database is primed and ready.")

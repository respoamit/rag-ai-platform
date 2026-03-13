
from qdrant_client import AsyncQdrantClient
from models.embeddings import embed

# Use Async client
client = AsyncQdrantClient("localhost", port=6333)

SIMILARITY_THRESHOLD = 0.7

async def retrieve(question):
    vector = embed(question)

    response = await client.query_points(
        collection_name="knowledge",
        query=vector,
        limit=5
)
    results = response.points

    filtered_context = []

    for r in results:
        if r.score >= SIMILARITY_THRESHOLD:
            filtered_context.append(r.payload["text"])

    return filtered_context

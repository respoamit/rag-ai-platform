#Converts document into embeddings and stores in qdrant
from qdrant_client import QdrantClient
from models.embeddings import embed
from utils.chunker import chunk_text
from qdrant_client.models import VectorParams, Distance

client = QdrantClient("localhost", port=6333)

documents = [
"""
Kubernetes is an open-source container orchestration platform that automates deployment, scaling and management of containerized applications.It groups containers into logical units of easier management.
""",
"""
Helm is a package manager in Kubernetes. It allows developers to package applications into reusable charts that simplify deployment and management.
"""
]

chunks = []

for doc in documents:
    chunks.extend(chunk_text(doc))

vectors = [embed(chunk) for chunk in chunks]

client.recreate_collection(
    collection_name="knowledge",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

for i, chunk in enumerate(chunks):

    client.upsert(
        collection_name="knowledge",
        points=[
            {
		"id": i,
		"vector": vectors[i],
		"payload": {"text": doc}
	    }
	]
    )
print("Chunked document indexed")

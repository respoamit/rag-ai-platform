from qdrant_client import QdrantClient
from models.embeddings import model
from utils.chunker import chunk_text

BATCH_SIZE = 8

client = QdrantClient("localhost", port=6333)

def batch_embed(texts):
    """
    Generates embeddings for a batch of texts.
    """
    return model.encode(texts).tolist()

def ingest_documents(documents):

    chunks = []

    for doc in documents:
        chunks.extend(chunk_text(doc))

    print(f"Total chunks created: {len(chunks)}")

    for i in range(0, len(chunks), BATCH_SIZE):

    batch = chunks[i:i+BATCH_SIZE]

    vectors = batch_embed(batch)

    points = []

    for j, chunk in enumerate(batch):

	points.append({
	    "id": i + j,
                "vector": vectors[j],
                "payload": {"text": chunk}
            })

        client.upsert(
            collection_name="knowledge",
            points=points
        )

        print(f"Indexed batch {i//BATCH_SIZE}")



if __name__=="__main__":
    documents = [
	"""
	kubernetes is an open-source container of orchestration platform that automates deployment and scaling of containerized applications.
	""",

	"""
	Helm simplifies Kubernetes application deployment using reusable charts.
	"""
    ]

    ingest_documents(documents)

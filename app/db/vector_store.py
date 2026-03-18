import os
from qdrant_client import QdrantClient
from dotenv import load_dotenv

load_dotenv()

qdrant_client = QdrantClient(
    host=os.getenv("QDRANT_HOST", "localhost"), 
    port=6333
)

def init_qdrant():
    collection_name = "stock_news"
    if not qdrant_client.collection_exists(collection_name):
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config={"size": 1536, "distance": "Cosine"}
        )
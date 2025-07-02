import pinecone
import os
from typing import List, Dict, Any

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-west1-gcp")
PINECONE_INDEX = os.getenv("PINECONE_INDEX", "products-index")

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Ensure index exists
if PINECONE_INDEX not in pinecone.list_indexes():
    pinecone.create_index(PINECONE_INDEX, dimension=384)  # Adjust dimension as needed

index = pinecone.Index(PINECONE_INDEX)

def upsert_product_vector(product_id: str, vector: List[float], metadata: Dict[str, Any]):
    index.upsert([(product_id, vector, metadata)])

def query_product_vectors(vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
    result = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return result["matches"]

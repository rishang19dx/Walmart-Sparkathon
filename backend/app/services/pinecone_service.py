from typing import List, Dict, Any
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

index_name = "developer-quickstart-py"

if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "llama-text-embed-v2",
            "field_map": {"text": "chunk_text"}
        }
    )

index = pc.Index(index_name)

def upsert_product_vector(product_id: str, vector: List[float], metadata: Dict[str, Any]):
    index.upsert([(product_id, vector, metadata)])

def query_product_vectors(vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
    result = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return result["matches"]

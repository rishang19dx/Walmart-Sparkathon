# ✅ FILE: app/services/pinecone_service.py

import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Import embedding model (adjust depending on what you're using)
from sentence_transformers import SentenceTransformer

load_dotenv()

# --- Pinecone setup ---
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX", "products-index")
PINECONE_HOST = os.getenv("PINECONE_HOST")  # Full host URL

# --- Initialize Pinecone client and index ---
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(index_name=PINECONE_INDEX, host=PINECONE_HOST)

# ✅ Load the embedding model (InstructorXL, all-MiniLM, etc.)
# Make sure to install: pip install sentence-transformers
model = SentenceTransformer("all-MiniLM-L6-v2")


# ✅ Function to generate 1024-dim embedding
def generate_embedding(text: str) -> list:
    return model.encode(text).tolist()

# ✅ Function to upsert a product vector
def upsert_product_vector(product_id: str, vector: list, metadata: dict):
    index.upsert([
        (product_id, vector, metadata)
    ])
    print(f"✅ Upserted '{product_id}' successfully.")

# ✅ Function to query top-k product vectors
def query_product_vectors(query_text: str, top_k: int = 5):
    # Generate embedding for the query
    query_vector = generate_embedding(query_text)
    
    response = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
    return response["matches"]

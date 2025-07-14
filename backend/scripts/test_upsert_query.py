from app.services.pinecone_service import upsert_product_vector, query_product_vectors, generate_embedding

# Sample product
product_id = "p123"
product_text = "Apple iPhone 14 with amazing camera and performance"
metadata = {"name": "iPhone 14", "category": "Smartphones"}

# Generate embedding for the product text
vector = generate_embedding(product_text)

# Upsert product vector
upsert_product_vector(product_id, vector, metadata)

# Query Pinecone
query = "best phone with camera quality"
results = query_product_vectors(query, top_k=3)

print("🔍 Top Matches:")
for match in results:
    print(match["score"], match["metadata"])

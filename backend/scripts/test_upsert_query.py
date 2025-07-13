from app.services.pinecone_service import upsert_product_vector, query_product_vectors

# Sample product
product_id = "p123"
product_text = "Apple iPhone 14 with amazing camera and performance"
metadata = {"name": "iPhone 14", "category": "Smartphones"}

# Upsert product vector (embedding done inside the function)
upsert_product_vector(product_id, product_text, metadata)

# Query Pinecone
query = "best phone with camera quality"
results = query_product_vectors(query, top_k=3)

print("🔍 Top Matches:")
for match in results:
    print(match["score"], match["metadata"])

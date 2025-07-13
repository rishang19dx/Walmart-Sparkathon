from app.services.pinecone_service import query_product_vectors

query = "comfortable running sneakers"
results = query_product_vectors(query)

print("🔍 Top matches:")
for match in results:
    print(f"→ ID: {match['id']}, Score: {match['score']}, Metadata: {match['metadata']}")

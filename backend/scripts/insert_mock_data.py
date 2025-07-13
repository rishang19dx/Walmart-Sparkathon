from app.models.db import get_collection
from app.services.pinecone_service import upsert_product_vector, generate_embedding  # Ensure this is imported

def insert_mock_data():
    # --- MongoDB Collections ---
    users_collection = get_collection("users")
    consents_collection = get_collection("consents")

    # Optional: Clean existing data
    users_collection.delete_many({})
    consents_collection.delete_many({})

    # --- Insert Mock Users ---
    mock_users = [
        {"_id": "u1", "name": "Aadra", "email": "aadra@example.com", "ceramic_stream_id": "dummy_stream_id_123"},
        {"_id": "u2", "name": "Shyam", "email": "shyam@example.com", "ceramic_stream_id": "dummy_stream_id_456"},
        {"_id": "u3", "name": "Riya", "email": "riya@example.com", "ceramic_stream_id": "dummy_stream_id_789"},
    ]
    users_collection.insert_many(mock_users)

    # --- Insert Mock Consents ---
    mock_consents = [
        {"user_id": "u1", "given": True},
        {"user_id": "u2", "given": False},
        {"user_id": "u3", "given": True}
    ]
    consents_collection.insert_many(mock_consents)

    print("✅ Users and consents inserted")

    # --- Insert Mock Products into Pinecone ---
    mock_products = [
        {"id": "p1", "name": "Red Shoes", "description": "Comfortable running shoes", "price": 49.99},
        {"id": "p2", "name": "Smart Watch", "description": "Track your health with this stylish smartwatch", "price": 199.99},
        {"id": "p3", "name": "Bluetooth Headphones", "description": "Wireless and noise-cancelling", "price": 89.99},
        {"id": "p4", "name": "Laptop Stand", "description": "Adjustable ergonomic laptop stand", "price": 29.99},
        {"id": "p5", "name": "Water Bottle", "description": "Insulated stainless steel water bottle", "price": 24.99},
    ]

    for product in mock_products:
        # Create embedding from name + description
        text = f"{product['name']} {product['description']}"
        vector = generate_embedding(text)

        # Push to Pinecone
        upsert_product_vector(
            product_id=product["id"],
            vector=vector,
            metadata=product
        )

    print("✅ Mock product vectors inserted into Pinecone")

if __name__ == "__main__":
    insert_mock_data()

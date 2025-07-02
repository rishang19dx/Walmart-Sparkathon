from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict, Any
from ..models.product import Product
from ..services.pinecone_service import upsert_product_vector, query_product_vectors

# This will be our mock database for now.
# In Week 2, this will be replaced by Pinecone and a real database.
MOCK_PRODUCTS = [
    {
        "product_id": "WMT001",
        "name": "Men's Classic Crewneck T-Shirt",
        "category": "Tops",
        "price": 12.50,
        "description": "A comfortable and stylish crewneck t-shirt made from 100% cotton.",
        "tags": ["mens", "shirt", "casual", "summer"]
    },
    {
        "product_id": "WMT002",
        "name": "Women's High-Rise Skinny Jeans",
        "category": "Jeans",
        "price": 35.00,
        "description": "Flattering high-rise skinny jeans with a hint of stretch for all-day comfort.",
        "tags": ["womens", "jeans", "formal", "winter"]
    },
    {
        "product_id": "WMT003",
        "name": "Unisex Aviator Sunglasses",
        "category": "Accessories",
        "price": 15.00,
        "description": "Classic aviator sunglasses with UV protection.",
        "tags": ["unisex", "accessories", "sunglasses", "summer"]
    }
]

router = APIRouter()

@router.get("/products", tags=["Products"])
async def get_all_products() -> List[Dict[str, Any]]:
    """
    Retrieve a list of all products from the mock catalog.
    """
    return MOCK_PRODUCTS

@router.get("/products/{product_id}", tags=["Products"])
async def get_product_by_id(product_id: str) -> Dict[str, Any]:
    """
    Retrieve a single product by its ID.
    """
    for product in MOCK_PRODUCTS:
        if product["product_id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/products", tags=["Products"])
async def create_product(product: Product):
    MOCK_PRODUCTS.append(product.dict())
    # For demo, use a dummy vector (should use real embedding in production)
    vector = [0.0] * 384
    upsert_product_vector(product.product_id, vector, product.dict())
    return product

@router.put("/products/{product_id}", tags=["Products"])
async def update_product(product_id: str, product: Product):
    for idx, p in enumerate(MOCK_PRODUCTS):
        if p["product_id"] == product_id:
            MOCK_PRODUCTS[idx] = product.dict()
            vector = [0.0] * 384
            upsert_product_vector(product.product_id, vector, product.dict())
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/products/{product_id}", tags=["Products"])
async def delete_product(product_id: str):
    for idx, p in enumerate(MOCK_PRODUCTS):
        if p["product_id"] == product_id:
            del MOCK_PRODUCTS[idx]
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/products/search", tags=["Products"])
async def search_products(query_vector: list = Body(...)):
    # In production, generate vector from query text using embedding model
    results = query_product_vectors(query_vector)
    return results
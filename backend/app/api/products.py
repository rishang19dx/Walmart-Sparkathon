from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

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
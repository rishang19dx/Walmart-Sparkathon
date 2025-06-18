from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    product_id: str
    name: str
    category: str
    price: float
    description: str
    image_url: Optional[str] = None
    tags: List[str] = []
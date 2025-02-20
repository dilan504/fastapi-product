
from sqlmodel import Field, SQLModel
from typing import Optional
from app.products_category.schemas import ProductCategoryRead
from app.products_brand.schemas import ProductBrandRead

class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None

# Modelo para crear una nueva tarea (hereda de ProductBase)
class ProductCreate(ProductBase):
    category_id: Optional[int] = None
    brand_id: Optional[int] = None

class ProductUpdate(ProductBase):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None

class ProductRead(ProductBase):
    id: int
    category: Optional[ProductCategoryRead] = None  # Relación con la categoría
    brand: Optional[ProductBrandRead] = None  # Relación con la categoría

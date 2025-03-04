
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.products.models import Product

class ProductBrand(SQLModel, table=True):
    __tablename__ = "product_brand"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    logo: str | None = Field(default=None)

    products: List["Product"] = Relationship(back_populates="brand")

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now(), nullable=True),
    )
from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.products_category.models import ProductCategory
from app.products_category.schemas import ProductCategoryCreate, ProductCategoryUpdate


class ProductCategoryService:
    no_task:str = "Product doesn't exits"
    # CREATE
    # ----------------------
    def create_product_category(self, item_data: ProductCategoryCreate, session: SessionDep):
        product_db = ProductCategory.model_validate(item_data.model_dump())
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ONE
    # ----------------------
    def get_product_category(self, item_id: int, session: SessionDep):
        product_db = session.get(ProductCategory, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return product_db

    # UPDATE
    # ----------------------
    def update_product_category(self, item_id: int, item_data: ProductCategoryUpdate, session: SessionDep):
        product_db = session.get(ProductCategory, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        product_db.sqlmodel_update(item_data_dict)
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ALL PLANS
    # ----------------------
    def get_product_categories(self, session: SessionDep):
        return session.exec(select(ProductCategory)).all()

    # DELETE
    # ----------------------
    def delete_product_category(self, item_id: int, session: SessionDep):
        product_db = session.get(ProductCategory, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        session.delete(product_db)
        session.commit()
        
        return {"detail": "ok"}

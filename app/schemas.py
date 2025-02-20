
from sqlmodel import Field, Session, SQLModel, select

from pydantic import EmailStr, field_validator
from app.db import engine
from app.customers.models import Customer
class CustomerBase(SQLModel):
    name: str = Field(default=None)
    last_name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

# Modelo para crear una nueva tarea (hereda de TaskBase)
class CustomerCreate(CustomerBase):
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        session = Session(engine)
        query = select(Customer).where(Customer.email == value)
        result = session.exec(query).first()
        if result:
            raise ValueError("This email is already registered")
        return value

class CustomerUpdate(CustomerBase):
    pass

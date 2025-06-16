from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    asin: str | None = None
    supplier_price: float | None = None
    amazon_price: float | None = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

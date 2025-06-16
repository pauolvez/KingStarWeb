from sqlalchemy import Column, Integer, String, Float

from ..db.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    asin = Column(String, nullable=True)
    supplier_price = Column(Float, nullable=True)
    amazon_price = Column(Float, nullable=True)

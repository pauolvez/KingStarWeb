from fastapi import FastAPI

from .api import users, products
from .db.session import Base, engine

app = FastAPI(title="King Star")

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users")
app.include_router(products.router, prefix="/products")

@app.get("/")
def read_root():
    return {"message": "King Star API"}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models import product as models
from ..schemas import product as schemas

router = APIRouter()

@router.get('/', response_model=list[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.post('/', response_model=schemas.Product)
def create_product(product_in: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = models.Product(**product_in.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

from ..core import scraping, amazon


@router.get('/search', response_model=list[schemas.Product])
def search_products(keyword: str, provider: str = "aliexpress", db: Session = Depends(get_db)):
    provider_results, _styles, _scripts = scraping.search_provider(provider, keyword)
    products: list[schemas.Product] = []
    for result in provider_results:
        amazon_data = amazon.search_product_by_asin(result['asin'])
        product = models.Product(
            name=result['name'],
            asin=result['asin'],
            supplier_price=result['price'],
            amazon_price=amazon_data['price'],
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        products.append(product)
    return products


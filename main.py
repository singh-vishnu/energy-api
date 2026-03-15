from fastapi import FastAPI, Depends, HTTPException,Path
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
from models import EnergyPrice
from schemas import EnergyPriceCreate, EnergyPriceUpdate

app = FastAPI(title="Oil & Gas Price API")

Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():

    return {"message": "Energy Price API running"}


# CREATE

@app.post("/prices")
def create_price(price: EnergyPriceCreate, db: Session = Depends(get_db)):

    existing = db.query(EnergyPrice).filter(
        EnergyPrice.id == price.id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Price ID already exists")

    db_price = EnergyPrice(**price.model_dump())

    db.add(db_price)
    db.commit()
    db.refresh(db_price)

    return {"message": "Price added"}


# VIEW ALL

@app.get("/prices")

def get_prices(db: Session = Depends(get_db)):

    prices = db.query(EnergyPrice).all()

    return prices


# VIEW ONE

@app.get("/prices/{price_id}")

def get_price(price_id: str= Path(..., description="Unique ID of the energy price record", example="E101"), db: Session = Depends(get_db)):

    price = db.query(EnergyPrice).filter(
        EnergyPrice.id == price_id
    ).first()

    if not price:
        raise HTTPException(404, "Price not found")

    return price


# UPDATE

@app.put("/prices/{price_id}")
def update_price(
    update: EnergyPriceUpdate,
    price_id: str = Path(..., description="ID of price record", examples=["E101"]),
    db: Session = Depends(get_db)
):

    price = db.query(EnergyPrice).filter(
        EnergyPrice.id == price_id
    ).first()

    if not price:
        raise HTTPException(404, "Price not found")

    for key, value in update.model_dump(
            exclude_unset=True).items():
        setattr(price, key, value)

    db.commit()

    return {"message": "Price updated"}


# DELETE

@app.delete("/prices/{price_id}")

def delete_price(price_id: str= Path(..., description="ID of price record to delete", example="E101"), db: Session = Depends(get_db)):

    price = db.query(EnergyPrice).filter(
        EnergyPrice.id == price_id
    ).first()

    if not price:
        raise HTTPException(404, "Price not found")

    db.delete(price)
    db.commit()

    return {"message": "Price deleted"}

@app.get("/prices/country/{country}")
def get_by_country(country: str, db: Session = Depends(get_db)):

    prices = db.query(EnergyPrice).filter(
        EnergyPrice.country == country
    ).all()

    return prices


@app.get("/")
def home():
    return {
        "message": "Energy Price Intelligence API",
        "docs": "/docs"
    }
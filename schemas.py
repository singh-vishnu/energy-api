from pydantic import BaseModel

class EnergyPriceCreate(BaseModel):

    id: str
    commodity: str
    benchmark: str
    country: str
    price: float
    currency: str
    unit: str
    date: str


class EnergyPriceUpdate(BaseModel):

    commodity: str | None = None
    benchmark: str | None = None
    country: str | None = None
    price: float | None = None
    currency: str | None = None
    unit: str | None = None
    date: str | None = None
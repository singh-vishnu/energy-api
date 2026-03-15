from pydantic import BaseModel, Field

class EnergyPriceCreate(BaseModel):

    id: str = Field(..., description="Unique identifier for the energy price record", examples=["E101"])

    commodity: str = Field(..., description="Type of energy commodity", examples=["crude_oil"])

    benchmark: str = Field(..., description="Pricing benchmark used in the market", examples=["Brent"])

    country: str = Field(..., description="Country associated with the price", examples=["India"])

    price: float = Field(..., description="Market price of the commodity", examples=[84.5])

    currency: str = Field(..., description="Currency in which price is quoted", examples=["USD"])

    unit: str = Field(..., description="Measurement unit of the commodity", examples=["barrel"])

    date: str = Field(..., description="Date of the price record", examples=["2026-03-15"])


class EnergyPriceUpdate(BaseModel):

    commodity: str | None = None
    benchmark: str | None = None
    country: str | None = None
    price: float | None = None
    currency: str | None = None
    unit: str | None = None
    date: str | None = None
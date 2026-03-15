from sqlalchemy import Column, String, Float
from database import Base

class EnergyPrice(Base):

    __tablename__ = "energy_prices"

    id = Column(String, primary_key=True, index=True)
    commodity = Column(String)
    benchmark = Column(String)
    country = Column(String)
    price = Column(Float)
    currency = Column(String)
    unit = Column(String)
    date = Column(String)
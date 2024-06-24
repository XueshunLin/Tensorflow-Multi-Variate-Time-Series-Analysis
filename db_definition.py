from typing import List
import datetime as dt
from sqlalchemy import create_engine, Column, Integer, Float, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, sessionmaker, declarative_base

DB_Paths = [
    "databases/cd230831.db",
    "databases/cd230926.db",
    "databases/cd240111.db"
]

class TemperatureChannelEnum:
    PT1   = 1
    PT2   = 2
    Still = 5
    MXC   = 6 # Mixing Chamber, 10mK stage

class PressureChannelEnum:
    VacuumCan = 1
    PumpingLine = 2
    CompressorOutlet = 3
    CompressorInlet = 4
    MixtureTank = 5
    VentingLine = 6

class CoolingWaterIO:
    Input = True
    Output = False

class CoolingWaterEnum:
    Compressor1 = 0
    Compressor2 = 1

KELVIN = 1
MILLIKELVIN = 1E3


# engine = create_engine(db_address)
# Session = sessionmaker(bind=engine)

Base = declarative_base()

class Temperature(Base):
    __tablename__ = "temperature"

    # Define columns using Column from sqlalchemy
    id = Column(Integer, primary_key=True)
    channel = Column(Integer)
    value = Column(Integer)  # Temperature in Kelvin
    datetime = Column(DateTime(timezone=True), server_default=func.now())

class Pressure(Base):
    __tablename__ = "maxigauge"

    id = Column(Integer, primary_key=True)
    channel = Column(Integer)
    value = Column(Integer)  
    datetime = Column(DateTime(timezone=True), server_default=func.now())

class CoolingWaterTemperature(Base):
    __tablename__ = "cooling"

    id = Column(Integer, primary_key=True)
    channel = Column(Integer)
    io = Column(Boolean)
    value = Column(Float)  # Temperature in Celsius
    datetime = Column(DateTime(timezone=True), server_default=func.now())

def create_session(db_path: str):
    """Create a session for a specific database path."""
    engine = create_engine(f'sqlite:///{db_path}')
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()



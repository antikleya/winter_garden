from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from src.database import Base
from .mixins import HasTimestamp


class Measurement(HasTimestamp, Base):
    __tablename__ = "measurements"
    speed = Column(Integer, nullable=False)
    inside_temperature = Column(Float, nullable=False)
    outside_temperature = Column(Float, nullable=False)
    inside_humidity = Column(Float, nullable=False)
    outside_humidity = Column(Float, nullable=False)
    humidifier_relay_state = Column(Boolean, nullable=False)
    pump_relay_state = Column(Boolean, nullable=False)

    debug_info = relationship("DebugInformation")

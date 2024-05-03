from sqlalchemy import Column, Integer, Float, Boolean, DateTime, ForeignKey
from src.database import Base


class DebugInformation(Base):
    __tablename__ = "debug_info"
    timestamp = Column(
        DateTime,
        ForeignKey("measurements.timestamp", ondelete="CASCADE"),
        primary_key=True,
    )
    delay = Column(Integer, nullable=False)
    pump_hysteresis_delta = Column(Integer, nullable=False)
    top_humidity_boundary = Column(Integer, nullable=False)
    bottom_humidity_boundary = Column(Integer, nullable=False)
    automatic_humidity_control = Column(Boolean, nullable=False)
    pid_kp = Column(Float, nullable=False)
    pid_ki = Column(Float, nullable=False)
    pid_kd = Column(Float, nullable=False)
    pump_automatic_control = Column(Boolean, nullable=False)
    pump_temperature_delta = Column(Float, nullable=False)
    target_temperature = Column(Float, nullable=False)
    temperature_sensor_offset = Column(Float, nullable=False)
    first_after_reboot = Column(Boolean, nullable=False)

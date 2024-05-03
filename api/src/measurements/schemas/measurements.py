from pydantic import BaseModel
from .debug_info import DebugInfo
from .debug_info import DebugInfoCreate


class Measurement(BaseModel):
    speed: int
    inside_temperature: float
    outside_temperature: float
    inside_humidity: float
    outside_humidity: float
    humidifier_relay_state: bool
    pump_relay_state: bool
    debug_info: DebugInfo


class MeasurementCreate(Measurement):
    debug_info: DebugInfoCreate

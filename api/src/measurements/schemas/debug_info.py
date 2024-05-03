from pydantic import BaseModel
from datetime import datetime


class DebugInfo(BaseModel):
    delay: int
    pump_hysteresis_delta: int
    top_humidity_boundary: int
    bottom_humidity_boundary: int
    automatic_humidity_control: bool
    pid_kp: float
    pid_ki: float
    pid_kd: float
    pump_automatic_control: bool
    pump_temperature_delta: float
    target_temperature: float
    temperature_sensor_offset: float
    first_after_reboot: bool


class DebugInfoCreate(DebugInfo):
    timestamp: datetime

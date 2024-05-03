from pydantic import BaseModel
from typing import Optional


class GardenConfig(BaseModel):
    delay: int
    pump_hysteresis_delta: int
    top_humidity_boundary: int
    bottom_humidity_boundary: int
    automatic_humidity_control: bool
    pid_kp: float
    pid_ki: float
    pid_kd: float
    pump_automatic_control: bool
    pump_temperature_delta: int
    target_temperature: int
    temperature_sensor_offset: float


class GardenConfigUpdate(BaseModel):
    delay: Optional[int]
    pump_hysteresis_delta: Optional[int]
    top_humidity_boundary: Optional[int]
    bottom_humidity_boundary: Optional[int]
    automatic_humidity_control: Optional[bool]
    pid_kp: Optional[float]
    pid_ki: Optional[float]
    pid_kd: Optional[float]
    pump_automatic_control: Optional[bool]
    pump_temperature_delta: Optional[int]
    target_temperature: Optional[int]
    temperature_sensor_offset: Optional[float]

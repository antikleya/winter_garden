from .schemas import Measurement, MeasurementCreate
from .schemas import DebugInfoCreate


def valid_measurement_create(measurement: Measurement) -> MeasurementCreate:
    debug_info_dict = measurement.debug_info.dict()
    debug_info_dict['timestamp'] = measurement.timestamp
    debug_info = DebugInfoCreate(**debug_info_dict)

    measurement_dict = measurement.dict()
    measurement_dict['debug_info'] = debug_info
    return MeasurementCreate(**measurement_dict)

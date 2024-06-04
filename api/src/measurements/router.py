from datetime import datetime
from fastapi import APIRouter, status, Depends
from .schemas import Measurement, MeasurementCreate
from .service import MeasurementService
from src.auth.router import current_user
from .dependecies import valid_measurement_create


router = APIRouter()


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=list[Measurement]
)
def get_measurements(
        begin: datetime,
        end: datetime,
        limit: int = 3000,
        service: MeasurementService = Depends(MeasurementService.get_new_instance)
):
    measurements = service.get_measurements(begin=begin, end=end, limit=limit)
    kek = Measurement(measurements[0])
    return measurements


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(current_user)]
)
def add_measurement(
        measurement: MeasurementCreate = Depends(valid_measurement_create),
        service: MeasurementService = Depends(MeasurementService.get_new_instance)
):
    return service.add_measurement(measurement=measurement)

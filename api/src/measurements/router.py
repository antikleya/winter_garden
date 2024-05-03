from datetime import datetime
from fastapi import APIRouter, status, Depends
from .schemas import Measurement
from .service import MeasurementService


router = APIRouter()


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=list[Measurement]
)
def get_measurements(
        begin: datetime,
        end: datetime,
        service: MeasurementService = Depends(MeasurementService.get_new_instance)
):
    return service.get_measurements(begin=begin, end=end)

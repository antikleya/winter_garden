from datetime import datetime

from src.base_service import BaseService
from .models import Measurement as MeasurementModel
from .schemas import MeasurementCreate

from sqlalchemy import and_


class MeasurementService(BaseService):
    model = MeasurementModel

    def get_measurements(self, begin: datetime, end: datetime) -> list[MeasurementModel]:
        measurements = self.session.query(self.model).filter(and_(
            self.model.timestamp >= begin,
            self.model.timestamp <= end
        )).all()
        return measurements

    def add_measurement(self, measurement: MeasurementCreate):
        params = measurement.dict()
        return self.create(params)


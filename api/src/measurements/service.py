from datetime import datetime

from src.base_service import BaseService
from .models import Measurement as MeasurementModel, DebugInformation
from .schemas import MeasurementCreate

from sqlalchemy import and_


class MeasurementService(BaseService):
    model = MeasurementModel

    def get_measurements(self, begin: datetime, end: datetime, limit: int) -> list[MeasurementModel]:
        measurements = self.session.query(self.model).filter(and_(
            self.model.timestamp >= begin,
            self.model.timestamp <= end
        )).all()
        return measurements

    def add_measurement(self, measurement: MeasurementCreate):
        params = measurement.dict()
        debug_info = DebugInformation(**params['debug_info'])
        params['debug_info'] = debug_info
        return self.create(params)

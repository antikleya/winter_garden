from datetime import datetime

from src.base_service import BaseService
from .models import Measurement

from sqlalchemy import and_


class MeasurementService(BaseService):
    def get_measurements(self, earliest_datetime: datetime, latest_datetime: datetime) -> list[Measurement]:
        measurements = self.session.query(Measurement).filter(and_(
            Measurement.timestamp >= earliest_datetime,
            Measurement.timestamp <= latest_datetime
        )).all()
        return measurements

    def add_measurement(self, ):
        pass

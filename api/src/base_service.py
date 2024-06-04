from typing import Any
from src.database import Session, get_session
from fastapi import Depends


class BaseService:
    model: Any

    def __init__(self, session: Session):
        self.session = session

    @classmethod
    def get_new_instance(cls, session: Session = Depends(get_session)):
        return cls(session)

    def create(self, create_data: dict):
        model = self.model()
        for key, value in create_data.items():
            if value is not None:
                setattr(model, key, value)
        self.session.add(model)
        self.session.commit()
        return model

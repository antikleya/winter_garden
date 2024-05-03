from src.database import Session, get_session
from fastapi import Depends


class BaseService:
    def __init__(self, session: Session):
        self.session = session

    @classmethod
    def get_new_instance(cls, session: Session = Depends(get_session)):
        yield cls.__class__(session)

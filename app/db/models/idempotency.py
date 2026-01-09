from sqlalchemy import Column, String, Integer, DateTime
from app.db.base import Base
import datetime

class IdempotencyKey(Base):
    __tablename__ = "idempotency_keys"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

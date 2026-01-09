from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import relationship
from app.db.base import Base
import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, default="pending")
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
    items = relationship("OrderItem", back_populates="order")

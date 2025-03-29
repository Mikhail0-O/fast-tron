from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app.core.db import Base


class Wallet(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    balance = Column(Integer, default=0)
    energy = Column(Integer, default=0)
    bandwidth = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.now())

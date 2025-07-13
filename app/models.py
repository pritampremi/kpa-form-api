from sqlalchemy import Column, Integer, Text
from .database import Base

class KPAForm(Base):
    __tablename__ = "kpa_forms"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    form_data = Column(Text, nullable=False)

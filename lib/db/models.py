from sqlalchemy import Column, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    type = Column(Enum('income', 'expense', name='transaction_type'), nullable=False)
    description = Column(String)


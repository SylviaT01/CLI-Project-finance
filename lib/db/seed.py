from models import Transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

transactions = [
    Transaction(date=date(2024, 6, 5), amount=1000, category='Salary', type='income', description='Monthly salary'),
    Transaction(date=date(2024, 6, 6), amount=50, category='Food', type='expense', description='Groceries'),
]

session.add_all(transactions)
session.commit()
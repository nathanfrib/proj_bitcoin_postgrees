from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

# Cria a base de dados 
Base = declarative_base()

class BitcoinPrice(Base):
    """Define a tabela bitcoin_prices"""
    __tablename__ = "bitcoin_prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.now())
    symbol = Column(String(10), nullable=False)
    price = Column(Float, nullable=False)


    
    

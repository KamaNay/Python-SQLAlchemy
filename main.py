from datetime import datetime

from db import Session
from models.declarative import Order, Product, Client

with Session() as session:
    product = session.get(Product, 1)
    
    session.delete(product)
    session.commit()
    
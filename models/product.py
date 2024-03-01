from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey

class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    precio = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
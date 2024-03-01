from typing import Optional
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: Optional[int] = None
    nombre_producto: str = Field(default="Omega 3", min_length=5, max_length=30)
    marca: str = Field(default="System", min_length=1, max_length=300)
    cantidad: int = Field(default=100)
    stock: int = Field(default=12)
    precio: int = Field(default=25000)
    category: str = Field(default="Suplementos dietético")

    # Configuracion de la documentacion
    class Config:
        model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "id": 1,
                        "Nombre Producto": "Mi producto",
                        "Marca": "Healthy",
                        "cantidad": 12,
                        "stock": 12,
                        "category": "Suplementos dietético"
                    }
                ]
            }
        }
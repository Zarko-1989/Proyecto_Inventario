from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.product import product_router
from routers.auth import auth_router


# Estamos creando una instancia de la clase FastAPI
app = FastAPI()
app.title = "Inventario El Proyecto" 
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(product_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi Inventario </h1>")


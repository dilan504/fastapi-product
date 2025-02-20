import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db import create_db_and_tables

from app.tasks import routers as Task
from app.products import routers as Product
from app.products_category import routers as ProductCategory
from app.products_brand import routers as ProductBrand
from app.customers import routers as Customer
app = FastAPI()

version = "v1"

description = """
API de un Sistema de tareas y productos, usando FastApi con Python.

Funciones;
- Crear, Leer, Actualizar y eliminar Tareas
"""

version_prefix = f"/api/{version}"


app = FastAPI(
    lifespan=create_db_and_tables,
    title="AppTransactionFastAPI",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Dilan Chuquimia Mita",
        "url": "https://github.com/dilan504",
        "email": "dilan.chuquimia@uab.edu.bo",
    },
    openapi_tags=[
        {
            "name": "Tasks",
            "description": "Lista de Tareas",
        },
        {
            "name": "Products",
            "description": "Lista de Products",
        },
        {
            "name": "Customers",
            "description": "Lista de Customers",
        },
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Prueba con "" temporalmente
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(Task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(Product.router, prefix="/products", tags=["Products"])
app.include_router(ProductCategory.router, prefix="/products_category", tags=["Products Category"])
app.include_router(ProductBrand.router, prefix="/products_brand", tags=["Products Brand"])
app.include_router(Customer.router, prefix="/customers", tags=["Customers"])


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Landing Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #b8f2e6;
            color: #5e6472;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .container {
            background: #aed9e0;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            margin: 0 0 10px;
        }
        .endpoint {
            background: #ffa69e;
            padding: 10px;
            border-radius: 5px;
            display: inline-block;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to my API</h1>
        <p>Simple and reliable endpoints for a store sim.</p>
        <div class="endpoint">https://fastapi-product-30fv.onrender.com/</div>
    </div>
</body>
</html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
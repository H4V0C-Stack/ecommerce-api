from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import auth, products, orders

app = FastAPI(
    title="E-commerce REST API",
    description="Katalog produktów z zamówieniami — wdrożony na Railway",
    version="1.0.0"
)

# Globalny handler błędów walidacji Pydantic
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": {"status": 500, "message": "Wewnętrzny błąd serwera"}}
    )

# Podłączamy routery
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/", tags=["Info"])
def root():
    return {
        "message": "E-commerce API działa!",
        "docs": "/docs",
        "version": "1.0.0"
    }

from fastapi import FastAPI
from typing import Any

from src.auth.router import login_router, registration_router
from src.measurements.router import router as measurement_router

app_configs: dict[str, Any] = {"title": "App API"}

app = FastAPI(**app_configs)

app.include_router(login_router, prefix='/auth', tags=['auth'])
app.include_router(registration_router, prefix='/auth', tags=['auth'])
app.include_router(measurement_router, prefix='/measurements', tags=['measurements'])


@app.get('/health')
def test_endpoint():
    return {"Hello": "World"}

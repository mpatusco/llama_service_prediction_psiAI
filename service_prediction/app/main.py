"""FastAPI main application.

This file initializes the FastAPI application and includes routers for handling 
requests related to predictions and evaluations.

Attributes:
    app (FastAPI): The main FastAPI application instance.
"""

from fastapi import FastAPI
from app.api.v1 import prediction_routes, evaluation_routes

app = FastAPI()

app.include_router(prediction_routes.router, prefix="/api/v1/prediction")
app.include_router(evaluation_routes.router, prefix="/api/v1/evaluation")

from fastapi import APIRouter, HTTPException
from app.services.prediction_service import make_prediction
from app.entities.prediction import PredictionRequest

router = APIRouter()

@router.post("/")
async def create_prediction_route(request: PredictionRequest):
    """Create a prediction based on a conversation.

    Args:
        request (PredictionRequest): The conversation data for prediction.

    Returns:
        dict: The prediction result.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await make_prediction(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

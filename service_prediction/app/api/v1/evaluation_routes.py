from fastapi import APIRouter, HTTPException
from app.services.evaluation_service import evaluate_persona
from app.entities.evaluation import EvaluationRequest

router = APIRouter()

@router.post("/")
async def evaluate_persona_route(request: EvaluationRequest):
    """Retrieve a diagnosis evaluation for a persona.

    Args:
        request (EvaluationRequest): The persona's diagnostic data.

    Returns:
        dict: The diagnosis for the specified persona.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await evaluate_persona(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

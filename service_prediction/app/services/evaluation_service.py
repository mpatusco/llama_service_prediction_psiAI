from app.entities.evaluation import EvaluationRequest
from app.repositories.mongo_repository import fetch_persona_by_key
from app.utils.base64_encoder import encode_name

async def evaluate_persona(request: EvaluationRequest):
    """Retrieve the diagnosis for a specific persona.

    Args:
        request (EvaluationRequest): The evaluation data.

    Returns:
        dict: The diagnosis for the persona.
    """
    key = encode_name(request.persona_name)
    persona_data = await fetch_persona_by_key(key)
    if persona_data:
        return {"diagnostico": persona_data.get("diagnostico")}
    return {"status": "Persona not found"}

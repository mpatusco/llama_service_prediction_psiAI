from pydantic import BaseModel

class EvaluationRequest(BaseModel):
    """Data model for an evaluation request.

    Attributes:
        diagnostico (str): Diagnosis of the persona.
        persona_name (str): Name of the persona.
    """
    diagnostico: str
    persona_name: str

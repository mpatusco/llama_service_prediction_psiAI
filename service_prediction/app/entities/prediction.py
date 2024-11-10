from pydantic import BaseModel

class PredictionRequest(BaseModel):
    """Data model for a prediction request.

    Attributes:
        conversa (str): The conversation text.
    """
    conversa: str

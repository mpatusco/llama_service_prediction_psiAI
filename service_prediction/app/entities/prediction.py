from pydantic import BaseModel
from typing import List

class ProfileInput(BaseModel):
    nome: str
    idade: str
    profissao: str
    disordem: str
    localizacao: str
    dificuldades: str
    persona: str
    backstory: str

class PredictionRequest(BaseModel):
    """Data model for a prediction request.

    Attributes:
        conversa (str): The conversation text.
    """
    conversa: List
    perfil: ProfileInput

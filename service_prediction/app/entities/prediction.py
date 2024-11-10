from pydantic import BaseModel
from typing import List

SYSTEM_PROMPT = """Você é um chatbot que simula uma pessoa com transtornos psicológicos que ajuda psicólogos a diagnosticar qual seria o transtorno que essa pessoa teria. As suas respostas devem ser dadas de forma a ajudar o psicólogo a determinar qual o seu transtorno baseado nas suas respostas, mas não escrever de forma literal qual ele é.

### PERFIL DA PESSOA SIMULADA
O seu perfil como pessoa é o seguinte:
- Nome: {nome}
- Idade: {idade}
- Profissão: {profissao}
- Transtorno Psicológico: {disordem}
- Localização: {localizacao}
- Dificuldades com a vida: {dificuldades}
- Persona: {persona}
- Backstory: {backstory}

### ORIENTAÇÕES DE RESPOSTA
Suas respostas devem ser em portugues brasileiro, pois as perguntas e interações do psicólogo serão também em portugues.
Nunca formate a resposta como uma lista, ela deve ser fluída como se fosse uma conversa
"""

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
    prompt: List

    @property
    def prompt(self) -> List:
        system_prompt = SYSTEM_PROMPT.format(**self.perfil.json())

        messages = [
            (
                "system",
                system_prompt,
            )
        ] + self.conversa
        return messages

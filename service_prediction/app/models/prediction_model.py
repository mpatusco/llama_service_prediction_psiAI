import os
from langchain_groq import ChatGroq

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

class PredictionModel:
    """A mock prediction model for conversation text.

    This model simulates a machine learning model that takes in conversation text
    and returns a prediction. In a real scenario, this would be replaced by an
    actual model (e.g., a neural network or other ML model).

    Methods:
        predict(conversa: str) -> str: Simulates the prediction on the input text.
    """

    def predict(self, conversa: list, perfil: dict) -> str:
        """Simulate a prediction based on the conversation text.

        Args:
            conversa (str): The input conversation text.

        Returns:
            str: Simulated prediction result.
        """

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=1,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        system_prompt = SYSTEM_PROMPT.format(**perfil)

        messages = [
            (
                "system",
                system_prompt,
            )
        ] + conversa
        ai_msg = llm.invoke(messages)
        return ai_msg.content

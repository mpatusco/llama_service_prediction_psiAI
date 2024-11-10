import os
from langchain_groq import ChatGroq
from typing import List


class PredictionModel:
    """A mock prediction model for conversation text.

    This model simulates a machine learning model that takes in conversation text
    and returns a prediction. In a real scenario, this would be replaced by an
    actual model (e.g., a neural network or other ML model).

    Methods:
        predict(conversa: str) -> str: Simulates the prediction on the input text.
    """

    def predict(self, prompt: List) -> str:
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

        ai_msg = llm.invoke(prompt)
        return ai_msg.content

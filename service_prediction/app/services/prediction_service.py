from app.entities.prediction import PredictionRequest
from app.models.prediction_model import PredictionModel

async def make_prediction(request: PredictionRequest):
    """Make a prediction based on conversation data.

    Args:
        request (PredictionRequest): The conversation data.

    Returns:
        dict: The prediction result.
    """
    model = PredictionModel()
    prediction = model.predict(request.prompt)
    return {"prediction": prediction}

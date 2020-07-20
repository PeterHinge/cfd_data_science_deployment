from pydantic import BaseModel


class PredictionResult(BaseModel):
    result: float

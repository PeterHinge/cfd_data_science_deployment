

from pydantic import BaseModel


class HousePredictionResult(BaseModel):
    median_house_value: float
    currency: str = "USD"

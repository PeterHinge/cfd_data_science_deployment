from typing import List
from pydantic import BaseModel


class PredictionPayload(BaseModel):
    input1: float
    input2: float


def payload_to_list(pp: PredictionPayload) -> List:
    return [
        pp.input1,
        pp.input2
    ]
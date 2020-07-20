from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.app.core import security
from src.app.models.payload import PredictionPayload
from src.app.models.prediction import PredictionResult
from src.app.services.models import PredictionModel

router = APIRouter()


@router.post("/predict", response_model=PredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: PredictionPayload = None
) -> PredictionResult:

    model: PredictionModel = request.app.state.model
    prediction: PredictionResult = model.predict(block_data)

    return prediction

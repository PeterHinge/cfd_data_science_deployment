from typing import List

from loguru import logger

from src.app.core.messages import NO_VALID_PAYLOAD
from src.app.models.payload import PredictionPayload, payload_to_list
from src.app.models.prediction import PredictionResult


class HousePriceModel(object):
    def __init__(self, path):
        self.path = path

    def _pre_process(self, payload: PredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = payload_to_list(payload)
        return result

    def _post_process(self, prediction: List) -> PredictionResult:
        logger.debug("Post-processing prediction.")
        pr = PredictionResult(result=prediction)
        return pr

    def _predict(self, features: List) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = features  # simply returns input feature. Inset your model prediction here
        return prediction_result

    def predict(self, payload: PredictionPayload) -> PredictionResult:
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result

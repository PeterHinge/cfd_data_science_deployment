from typing import List

from loguru import logger

from src.app.core.messages import NO_VALID_PAYLOAD
from src.app.models.payload import PredictionPayload, payload_to_list
from src.app.models.prediction import PredictionResult


class PredictionModel(object):
    def __init__(self, path):
        self.path = path

    def _pre_process(self, payload: PredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        pre_processed_payload = payload_to_list(payload)
        return pre_processed_payload

    def _post_process(self, prediction: List) -> PredictionResult:
        logger.debug("Post-processing prediction.")
        post_processed_result = PredictionResult(result=prediction)
        return post_processed_result

    def _predict(self, features: List) -> List:
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

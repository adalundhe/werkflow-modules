from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_real_time_inference_recommendation_model import SageMakerRealTimeInferenceRecommendationModel


class SageMakerDeploymentRecommendationModel(BaseModel):
    RecommendationStatus: StrictStr | None = None
    RealTimeInferenceRecommendations: list[SageMakerRealTimeInferenceRecommendationModel] | None = None

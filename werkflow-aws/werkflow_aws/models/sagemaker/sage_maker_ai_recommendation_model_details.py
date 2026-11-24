from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_recommendation_instance_detail import SageMakerAIRecommendationInstanceDetail


class SageMakerAIRecommendationModelDetails(BaseModel):
    ModelPackageArn: StrictStr | None = None
    InferenceSpecificationName: StrictStr | None = None
    InstanceDetails: list[SageMakerAIRecommendationInstanceDetail] | None = None

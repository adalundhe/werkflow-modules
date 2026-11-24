from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_mlflow_config import SageMakerAIMlflowConfig


class SageMakerAIRecommendationOutputResult(BaseModel):
    S3OutputLocation: StrictStr | None = None
    ModelPackageGroupIdentifier: StrictStr | None = None
    MlflowConfig: SageMakerAIMlflowConfig | None = None

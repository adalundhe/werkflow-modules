from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_optimization_model_access_config import SageMakerOptimizationModelAccessConfig


class SageMakerOptimizationJobModelSourceS3(BaseModel):
    S3Uri: StrictStr | None = None
    ModelAccessConfig: SageMakerOptimizationModelAccessConfig | None = None

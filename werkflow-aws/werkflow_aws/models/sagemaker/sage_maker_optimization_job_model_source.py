from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_optimization_job_model_source_s3 import SageMakerOptimizationJobModelSourceS3
from .sage_maker_optimization_sage_maker_model import SageMakerOptimizationSageMakerModel


class SageMakerOptimizationJobModelSource(BaseModel):
    S3: SageMakerOptimizationJobModelSourceS3 | None = None
    SageMakerModel: SageMakerOptimizationSageMakerModel | None = None

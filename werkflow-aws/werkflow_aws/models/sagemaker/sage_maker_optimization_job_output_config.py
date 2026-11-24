from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_optimization_sage_maker_model import SageMakerOptimizationSageMakerModel


class SageMakerOptimizationJobOutputConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
    S3OutputLocation: StrictStr | None = None
    SageMakerModel: SageMakerOptimizationSageMakerModel | None = None

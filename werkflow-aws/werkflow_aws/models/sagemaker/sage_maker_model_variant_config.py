from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_infrastructure_config import SageMakerModelInfrastructureConfig


class SageMakerModelVariantConfig(BaseModel):
    ModelName: StrictStr
    VariantName: StrictStr
    InfrastructureConfig: SageMakerModelInfrastructureConfig

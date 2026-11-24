from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_infrastructure_config import SageMakerModelInfrastructureConfig


class SageMakerModelVariantConfigSummary(BaseModel):
    ModelName: StrictStr | None = None
    VariantName: StrictStr | None = None
    InfrastructureConfig: SageMakerModelInfrastructureConfig | None = None
    Status: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .sage_maker_production_variant_serverless_update_config import SageMakerProductionVariantServerlessUpdateConfig


class SageMakerDesiredWeightAndCapacity(BaseModel):
    VariantName: StrictStr
    DesiredWeight: StrictFloat | StrictInt | None = None
    DesiredInstanceCount: StrictInt | None = None
    ServerlessUpdateConfig: SageMakerProductionVariantServerlessUpdateConfig | None = None

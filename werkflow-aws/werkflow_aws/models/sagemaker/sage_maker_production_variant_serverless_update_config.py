from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerProductionVariantServerlessUpdateConfig(BaseModel):
    MaxConcurrency: StrictInt | None = None
    ProvisionedConcurrency: StrictInt | None = None

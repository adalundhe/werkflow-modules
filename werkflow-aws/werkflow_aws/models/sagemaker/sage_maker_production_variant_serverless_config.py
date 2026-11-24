from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerProductionVariantServerlessConfig(BaseModel):
    MemorySizeInMB: StrictInt | None = None
    MaxConcurrency: StrictInt | None = None
    ProvisionedConcurrency: StrictInt | None = None

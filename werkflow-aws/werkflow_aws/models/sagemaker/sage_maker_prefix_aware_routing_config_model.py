from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerPrefixAwareRoutingConfigModel(BaseModel):
    PrefixLength: StrictInt | None = None
    ConcurrencyThreshold: StrictInt | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerPrefixAwareRoutingConfig(BaseModel):
    PrefixLength: StrictInt | None = None
    ConcurrencyThreshold: StrictInt | None = None

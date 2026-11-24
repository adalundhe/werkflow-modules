from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerInferenceComponentAvailabilityZoneBalance(BaseModel):
    EnforcementMode: StrictStr | None = None
    MaxImbalance: StrictInt | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerClusterDrainPolicy(BaseModel):
    DrainTimeoutInSeconds: StrictInt | None = None
    OnDrainTimeout: StrictStr | None = None

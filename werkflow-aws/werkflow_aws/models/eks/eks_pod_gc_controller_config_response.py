from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSPodGcControllerConfigResponse(BaseModel):
    terminatedPodGcThreshold: StrictInt | None = None

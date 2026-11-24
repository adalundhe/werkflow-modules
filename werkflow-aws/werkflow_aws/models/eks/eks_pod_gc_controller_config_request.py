from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSPodGcControllerConfigRequest(BaseModel):
    terminatedPodGcThreshold: StrictInt | None = None

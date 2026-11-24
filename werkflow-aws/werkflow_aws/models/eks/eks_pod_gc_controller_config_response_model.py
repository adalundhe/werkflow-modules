from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSPodGcControllerConfigResponseModel(BaseModel):
    terminatedPodGcThreshold: StrictInt | None = None

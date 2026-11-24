from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_share_attributes import BatchShareAttributes


class BatchFairsharePolicy(BaseModel):
    shareDecaySeconds: StrictInt | None = None
    computeReservation: StrictInt | None = None
    shareDistribution: list[BatchShareAttributes] | None = None

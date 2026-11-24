from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .eks_warm_pool_state import EKSWarmPoolState


class EKSWarmPoolConfig(BaseModel):
    enabled: StrictBool | None = None
    minSize: StrictInt | None = None
    maxGroupPreparedCapacity: StrictInt | None = None
    poolState: EKSWarmPoolState | None = None
    reuseOnScaleIn: StrictBool | None = None

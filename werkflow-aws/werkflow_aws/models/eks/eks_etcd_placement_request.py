from __future__ import annotations
from pydantic import BaseModel
from .eks_spread_level import EKSSpreadLevel


class EKSEtcdPlacementRequest(BaseModel):
    spreadLevel: EKSSpreadLevel | None = None

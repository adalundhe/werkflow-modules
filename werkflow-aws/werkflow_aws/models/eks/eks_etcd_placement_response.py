from __future__ import annotations
from pydantic import BaseModel
from .eks_spread_level import EKSSpreadLevel


class EKSEtcdPlacementResponse(BaseModel):
    spreadLevel: EKSSpreadLevel | None = None

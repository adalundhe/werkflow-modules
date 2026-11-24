from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_spread_level import EKSSpreadLevel


class EKSControlPlanePlacementRequest(BaseModel):
    groupName: StrictStr | None = None
    spreadLevel: EKSSpreadLevel | None = None

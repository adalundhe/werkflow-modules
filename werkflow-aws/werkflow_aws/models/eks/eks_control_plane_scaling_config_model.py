from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSControlPlaneScalingConfigModel(BaseModel):
    tier: StrictStr | None = None

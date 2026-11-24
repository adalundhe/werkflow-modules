from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAutoScalingGroup(BaseModel):
    name: StrictStr | None = None

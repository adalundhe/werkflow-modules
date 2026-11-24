from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AutoScalingInstanceReusePolicy(BaseModel):
    ReuseOnScaleIn: StrictBool | None = None

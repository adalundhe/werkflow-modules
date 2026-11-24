from __future__ import annotations
from pydantic import BaseModel
from .ecs_nvidia_mps_allocation import ECSNvidiaMpsAllocation


class ECSSharingStrategy(BaseModel):
    nvidiaMps: ECSNvidiaMpsAllocation | None = None

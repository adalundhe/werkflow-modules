from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerECSServiceRecommendationFilter(BaseModel):
    name: Literal['Finding', 'FindingReasonCode'] | None = None
    values: list[StrictStr] | None = None

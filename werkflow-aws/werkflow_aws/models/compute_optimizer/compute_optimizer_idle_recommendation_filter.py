from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerIdleRecommendationFilter(BaseModel):
    name: Literal['Finding', 'ResourceType'] | None = None
    values: list[StrictStr] | None = None

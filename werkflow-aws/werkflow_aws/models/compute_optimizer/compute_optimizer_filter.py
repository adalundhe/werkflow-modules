from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerFilter(BaseModel):
    name: Literal['Finding', 'FindingReasonCodes', 'RecommendationSourceType', 'InferredWorkloadTypes'] | None = None
    values: list[StrictStr] | None = None

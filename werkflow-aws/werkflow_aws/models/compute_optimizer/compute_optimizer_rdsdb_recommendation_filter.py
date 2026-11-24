from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerRDSDBRecommendationFilter(BaseModel):
    name: Literal['InstanceFinding', 'InstanceFindingReasonCode', 'StorageFinding', 'StorageFindingReasonCode', 'Idle'] | None = None
    values: list[StrictStr] | None = None

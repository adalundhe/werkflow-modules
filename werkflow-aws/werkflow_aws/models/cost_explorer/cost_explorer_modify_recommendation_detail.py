from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_target_instance import CostExplorerTargetInstance


class CostExplorerModifyRecommendationDetail(BaseModel):
    TargetInstances: list[CostExplorerTargetInstance] | None = None

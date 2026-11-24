from __future__ import annotations
from pydantic import BaseModel
from .eks_resource_weight import EKSResourceWeight
from .eks_scoring_strategy_type import EKSScoringStrategyType


class EKSScoringStrategy(BaseModel):
    type: EKSScoringStrategyType | None = None
    resources: list[EKSResourceWeight] | None = None

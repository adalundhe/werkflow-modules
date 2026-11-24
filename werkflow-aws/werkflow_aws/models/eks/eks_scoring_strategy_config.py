from __future__ import annotations
from pydantic import BaseModel
from .eks_scoring_strategy_constraints import EKSScoringStrategyConstraints
from .eks_scoring_strategy_model import EKSScoringStrategyModel


class EKSScoringStrategyConfig(BaseModel):
    defaultValue: EKSScoringStrategyModel | None = None
    constraints: EKSScoringStrategyConstraints | None = None

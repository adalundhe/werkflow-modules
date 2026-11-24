from __future__ import annotations
from pydantic import BaseModel
from .eks_scoring_strategy_config import EKSScoringStrategyConfig


class EKSNodeResourcesFitVersionConfig(BaseModel):
    scoringStrategy: EKSScoringStrategyConfig | None = None

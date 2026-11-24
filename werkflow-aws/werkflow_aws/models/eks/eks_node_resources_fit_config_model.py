from __future__ import annotations
from pydantic import BaseModel
from .eks_scoring_strategy_model import EKSScoringStrategyModel


class EKSNodeResourcesFitConfigModel(BaseModel):
    scoringStrategy: EKSScoringStrategyModel | None = None

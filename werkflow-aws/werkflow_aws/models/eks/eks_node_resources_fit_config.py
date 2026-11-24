from __future__ import annotations
from pydantic import BaseModel
from .eks_scoring_strategy import EKSScoringStrategy


class EKSNodeResourcesFitConfig(BaseModel):
    scoringStrategy: EKSScoringStrategy | None = None

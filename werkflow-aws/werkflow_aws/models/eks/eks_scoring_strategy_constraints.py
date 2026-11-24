from __future__ import annotations
from pydantic import BaseModel
from .eks_allowed_values_constraint import EKSAllowedValuesConstraint
from .eks_resource_constraints import EKSResourceConstraints


class EKSScoringStrategyConstraints(BaseModel):
    scoringStrategy: EKSAllowedValuesConstraint | None = None
    resources: EKSResourceConstraints | None = None

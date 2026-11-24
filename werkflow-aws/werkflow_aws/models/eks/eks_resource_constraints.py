from __future__ import annotations
from pydantic import BaseModel
from .eks_allowed_values_constraint import EKSAllowedValuesConstraint
from .eks_integer_range_constraint import EKSIntegerRangeConstraint


class EKSResourceConstraints(BaseModel):
    name: EKSAllowedValuesConstraint | None = None
    weight: EKSIntegerRangeConstraint | None = None

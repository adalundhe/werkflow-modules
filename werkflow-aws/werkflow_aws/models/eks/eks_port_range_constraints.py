from __future__ import annotations
from pydantic import BaseModel
from .eks_integer_range_constraint import EKSIntegerRangeConstraint


class EKSPortRangeConstraints(BaseModel):
    minPort: EKSIntegerRangeConstraint | None = None
    maxPort: EKSIntegerRangeConstraint | None = None

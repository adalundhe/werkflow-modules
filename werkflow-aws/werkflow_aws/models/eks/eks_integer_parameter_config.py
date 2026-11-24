from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .eks_integer_constraints import EKSIntegerConstraints


class EKSIntegerParameterConfig(BaseModel):
    defaultValue: StrictInt | None = None
    constraints: EKSIntegerConstraints | None = None

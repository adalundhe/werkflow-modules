from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_duration_constraints import EKSDurationConstraints


class EKSDurationParameterConfig(BaseModel):
    defaultValue: StrictStr | None = None
    constraints: EKSDurationConstraints | None = None

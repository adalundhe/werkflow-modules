from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .eks_log_type import EKSLogType


class EKSLogSetup(BaseModel):
    types: list[EKSLogType] | None = None
    enabled: StrictBool | None = None

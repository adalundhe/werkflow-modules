from __future__ import annotations
from pydantic import BaseModel
from .eks_log_setup import EKSLogSetup


class EKSLogging(BaseModel):
    clusterLogging: list[EKSLogSetup] | None = None

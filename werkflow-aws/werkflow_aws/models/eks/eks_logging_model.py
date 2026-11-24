from __future__ import annotations
from pydantic import BaseModel
from .eks_log_setup_model import EKSLogSetupModel


class EKSLoggingModel(BaseModel):
    clusterLogging: list[EKSLogSetupModel] | None = None

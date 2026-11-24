from __future__ import annotations
from pydantic import BaseModel
from .eks_integer_parameter_config import EKSIntegerParameterConfig


class EKSPodGcControllerVersionConfig(BaseModel):
    terminatedPodGcThreshold: EKSIntegerParameterConfig | None = None

from __future__ import annotations
from pydantic import BaseModel
from .eks_duration_parameter_config import EKSDurationParameterConfig


class EKSHorizontalPodAutoscalerControllerVersionConfig(BaseModel):
    horizontalPodAutoscalerSyncPeriod: EKSDurationParameterConfig | None = None

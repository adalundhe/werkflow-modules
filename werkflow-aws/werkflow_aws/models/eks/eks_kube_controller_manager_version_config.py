from __future__ import annotations
from pydantic import BaseModel
from .eks_horizontal_pod_autoscaler_controller_version_config import EKSHorizontalPodAutoscalerControllerVersionConfig
from .eks_pod_gc_controller_version_config import EKSPodGcControllerVersionConfig


class EKSKubeControllerManagerVersionConfig(BaseModel):
    podGcControllerConfig: EKSPodGcControllerVersionConfig | None = None
    horizontalPodAutoscalerControllerConfig: EKSHorizontalPodAutoscalerControllerVersionConfig | None = None

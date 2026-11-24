from __future__ import annotations
from pydantic import BaseModel
from .eks_horizontal_pod_autoscaler_controller_config_request import EKSHorizontalPodAutoscalerControllerConfigRequest
from .eks_pod_gc_controller_config_request import EKSPodGcControllerConfigRequest


class EKSKubeControllerManagerConfigRequest(BaseModel):
    podGcControllerConfig: EKSPodGcControllerConfigRequest | None = None
    horizontalPodAutoscalerControllerConfig: (
        EKSHorizontalPodAutoscalerControllerConfigRequest | None
    ) = None

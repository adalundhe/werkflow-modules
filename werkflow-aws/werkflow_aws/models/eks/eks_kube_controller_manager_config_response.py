from __future__ import annotations
from pydantic import BaseModel
from .eks_horizontal_pod_autoscaler_controller_config_response import EKSHorizontalPodAutoscalerControllerConfigResponse
from .eks_pod_gc_controller_config_response import EKSPodGcControllerConfigResponse


class EKSKubeControllerManagerConfigResponse(BaseModel):
    podGcControllerConfig: EKSPodGcControllerConfigResponse | None = None
    horizontalPodAutoscalerControllerConfig: (
        EKSHorizontalPodAutoscalerControllerConfigResponse | None
    ) = None

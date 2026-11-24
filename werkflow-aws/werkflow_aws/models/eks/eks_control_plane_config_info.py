from __future__ import annotations
from pydantic import BaseModel
from .eks_kube_api_server_version_config import EKSKubeApiServerVersionConfig
from .eks_kube_controller_manager_version_config import EKSKubeControllerManagerVersionConfig
from .eks_kube_scheduler_version_config import EKSKubeSchedulerVersionConfig


class EKSControlPlaneConfigInfo(BaseModel):
    kubeApiServerConfig: EKSKubeApiServerVersionConfig | None = None
    kubeSchedulerConfig: EKSKubeSchedulerVersionConfig | None = None
    kubeControllerManagerConfig: EKSKubeControllerManagerVersionConfig | None = None

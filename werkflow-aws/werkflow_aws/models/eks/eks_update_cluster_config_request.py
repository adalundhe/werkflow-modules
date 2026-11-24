from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_compute_config_request import EKSComputeConfigRequest
from .eks_control_plane_scaling_config import EKSControlPlaneScalingConfig
from .eks_kube_api_server_config_request import EKSKubeApiServerConfigRequest
from .eks_kube_controller_manager_config_request import EKSKubeControllerManagerConfigRequest
from .eks_kube_scheduler_config_request import EKSKubeSchedulerConfigRequest
from .eks_kubernetes_network_config_request import EKSKubernetesNetworkConfigRequest
from .eks_logging import EKSLogging
from .eks_remote_network_config_request import EKSRemoteNetworkConfigRequest
from .eks_storage_config_request import EKSStorageConfigRequest
from .eks_update_access_config_request import EKSUpdateAccessConfigRequest
from .eks_upgrade_policy_request import EKSUpgradePolicyRequest
from .eks_vpc_config_request import EKSVpcConfigRequest
from .eks_zonal_shift_config_request import EKSZonalShiftConfigRequest


class EKSUpdateClusterConfigRequest(BaseModel):
    name: StrictStr
    resourcesVpcConfig: EKSVpcConfigRequest | None = None
    logging: EKSLogging | None = None
    clientRequestToken: StrictStr | None = None
    accessConfig: EKSUpdateAccessConfigRequest | None = None
    upgradePolicy: EKSUpgradePolicyRequest | None = None
    zonalShiftConfig: EKSZonalShiftConfigRequest | None = None
    computeConfig: EKSComputeConfigRequest | None = None
    kubernetesNetworkConfig: EKSKubernetesNetworkConfigRequest | None = None
    storageConfig: EKSStorageConfigRequest | None = None
    remoteNetworkConfig: EKSRemoteNetworkConfigRequest | None = None
    deletionProtection: StrictBool | None = None
    controlPlaneScalingConfig: EKSControlPlaneScalingConfig | None = None
    kubeApiServerConfig: EKSKubeApiServerConfigRequest | None = None
    kubeSchedulerConfig: EKSKubeSchedulerConfigRequest | None = None
    kubeControllerManagerConfig: EKSKubeControllerManagerConfigRequest | None = None

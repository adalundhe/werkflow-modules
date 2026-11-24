from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_compute_config_request import EKSComputeConfigRequest
from .eks_control_plane_scaling_config import EKSControlPlaneScalingConfig
from .eks_create_access_config_request import EKSCreateAccessConfigRequest
from .eks_encryption_config import EKSEncryptionConfig
from .eks_kube_api_server_config_request import EKSKubeApiServerConfigRequest
from .eks_kube_controller_manager_config_request import EKSKubeControllerManagerConfigRequest
from .eks_kube_scheduler_config_request import EKSKubeSchedulerConfigRequest
from .eks_kubernetes_network_config_request import EKSKubernetesNetworkConfigRequest
from .eks_logging import EKSLogging
from .eks_outpost_config_request import EKSOutpostConfigRequest
from .eks_remote_network_config_request import EKSRemoteNetworkConfigRequest
from .eks_storage_config_request import EKSStorageConfigRequest
from .eks_upgrade_policy_request import EKSUpgradePolicyRequest
from .eks_vpc_config_request import EKSVpcConfigRequest
from .eks_zonal_shift_config_request import EKSZonalShiftConfigRequest


class EKSCreateClusterRequest(BaseModel):
    name: StrictStr
    roleArn: StrictStr
    resourcesVpcConfig: EKSVpcConfigRequest
    version: StrictStr | None = None
    kubernetesNetworkConfig: EKSKubernetesNetworkConfigRequest | None = None
    logging: EKSLogging | None = None
    clientRequestToken: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    encryptionConfig: list[EKSEncryptionConfig] | None = None
    outpostConfig: EKSOutpostConfigRequest | None = None
    accessConfig: EKSCreateAccessConfigRequest | None = None
    bootstrapSelfManagedAddons: StrictBool | None = None
    upgradePolicy: EKSUpgradePolicyRequest | None = None
    zonalShiftConfig: EKSZonalShiftConfigRequest | None = None
    remoteNetworkConfig: EKSRemoteNetworkConfigRequest | None = None
    computeConfig: EKSComputeConfigRequest | None = None
    storageConfig: EKSStorageConfigRequest | None = None
    deletionProtection: StrictBool | None = None
    controlPlaneScalingConfig: EKSControlPlaneScalingConfig | None = None
    kubeApiServerConfig: EKSKubeApiServerConfigRequest | None = None
    kubeSchedulerConfig: EKSKubeSchedulerConfigRequest | None = None
    kubeControllerManagerConfig: EKSKubeControllerManagerConfigRequest | None = None

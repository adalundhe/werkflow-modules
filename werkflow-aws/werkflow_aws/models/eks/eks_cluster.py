from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_access_config_response import EKSAccessConfigResponse
from .eks_certificate import EKSCertificate
from .eks_cluster_health import EKSClusterHealth
from .eks_cluster_status import EKSClusterStatus
from .eks_compute_config_response import EKSComputeConfigResponse
from .eks_connector_config_response import EKSConnectorConfigResponse
from .eks_control_plane_scaling_config import EKSControlPlaneScalingConfig
from .eks_encryption_config import EKSEncryptionConfig
from .eks_identity import EKSIdentity
from .eks_kube_api_server_config_response import EKSKubeApiServerConfigResponse
from .eks_kube_controller_manager_config_response import EKSKubeControllerManagerConfigResponse
from .eks_kube_scheduler_config_response import EKSKubeSchedulerConfigResponse
from .eks_kubernetes_network_config_response import EKSKubernetesNetworkConfigResponse
from .eks_logging import EKSLogging
from .eks_outpost_config_response import EKSOutpostConfigResponse
from .eks_remote_network_config_response import EKSRemoteNetworkConfigResponse
from .eks_storage_config_response import EKSStorageConfigResponse
from .eks_upgrade_policy_response import EKSUpgradePolicyResponse
from .eks_vpc_config_response import EKSVpcConfigResponse
from .eks_zonal_shift_config_response import EKSZonalShiftConfigResponse


class EKSCluster(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | None = None
    version: StrictStr | None = None
    endpoint: StrictStr | None = None
    roleArn: StrictStr | None = None
    resourcesVpcConfig: EKSVpcConfigResponse | None = None
    kubernetesNetworkConfig: EKSKubernetesNetworkConfigResponse | None = None
    logging: EKSLogging | None = None
    identity: EKSIdentity | None = None
    status: EKSClusterStatus | None = None
    certificateAuthority: EKSCertificate | None = None
    clientRequestToken: StrictStr | None = None
    platformVersion: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    encryptionConfig: list[EKSEncryptionConfig] | None = None
    connectorConfig: EKSConnectorConfigResponse | None = None
    id: StrictStr | None = None
    health: EKSClusterHealth | None = None
    outpostConfig: EKSOutpostConfigResponse | None = None
    accessConfig: EKSAccessConfigResponse | None = None
    upgradePolicy: EKSUpgradePolicyResponse | None = None
    zonalShiftConfig: EKSZonalShiftConfigResponse | None = None
    remoteNetworkConfig: EKSRemoteNetworkConfigResponse | None = None
    computeConfig: EKSComputeConfigResponse | None = None
    storageConfig: EKSStorageConfigResponse | None = None
    deletionProtection: StrictBool | None = None
    controlPlaneScalingConfig: EKSControlPlaneScalingConfig | None = None
    kubeApiServerConfig: EKSKubeApiServerConfigResponse | None = None
    kubeSchedulerConfig: EKSKubeSchedulerConfigResponse | None = None
    kubeControllerManagerConfig: EKSKubeControllerManagerConfigResponse | None = None

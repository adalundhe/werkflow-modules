from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_access_config_response_model import EKSAccessConfigResponseModel
from .eks_certificate_model import EKSCertificateModel
from .eks_cluster_health_model import EKSClusterHealthModel
from .eks_compute_config_response_model import EKSComputeConfigResponseModel
from .eks_connector_config_response_model import EKSConnectorConfigResponseModel
from .eks_control_plane_scaling_config_model import EKSControlPlaneScalingConfigModel
from .eks_encryption_config_model import EKSEncryptionConfigModel
from .eks_identity_model import EKSIdentityModel
from .eks_kube_api_server_config_response_model import EKSKubeApiServerConfigResponseModel
from .eks_kube_controller_manager_config_response_model import EKSKubeControllerManagerConfigResponseModel
from .eks_kube_scheduler_config_response_model import EKSKubeSchedulerConfigResponseModel
from .eks_kubernetes_network_config_response_model import EKSKubernetesNetworkConfigResponseModel
from .eks_logging_model import EKSLoggingModel
from .eks_outpost_config_response_model import EKSOutpostConfigResponseModel
from .eks_remote_network_config_response_model import EKSRemoteNetworkConfigResponseModel
from .eks_storage_config_response_model import EKSStorageConfigResponseModel
from .eks_upgrade_policy_response_model import EKSUpgradePolicyResponseModel
from .eks_vpc_config_response_model import EKSVpcConfigResponseModel
from .eks_zonal_shift_config_response_model import EKSZonalShiftConfigResponseModel


class EKSClusterModel(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    version: StrictStr | None = None
    endpoint: StrictStr | None = None
    roleArn: StrictStr | None = None
    resourcesVpcConfig: EKSVpcConfigResponseModel | None = None
    kubernetesNetworkConfig: EKSKubernetesNetworkConfigResponseModel | None = None
    logging: EKSLoggingModel | None = None
    identity: EKSIdentityModel | None = None
    status: StrictStr | None = None
    certificateAuthority: EKSCertificateModel | None = None
    clientRequestToken: StrictStr | None = None
    platformVersion: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    encryptionConfig: list[EKSEncryptionConfigModel] | None = None
    connectorConfig: EKSConnectorConfigResponseModel | None = None
    id: StrictStr | None = None
    health: EKSClusterHealthModel | None = None
    outpostConfig: EKSOutpostConfigResponseModel | None = None
    accessConfig: EKSAccessConfigResponseModel | None = None
    upgradePolicy: EKSUpgradePolicyResponseModel | None = None
    zonalShiftConfig: EKSZonalShiftConfigResponseModel | None = None
    remoteNetworkConfig: EKSRemoteNetworkConfigResponseModel | None = None
    computeConfig: EKSComputeConfigResponseModel | None = None
    storageConfig: EKSStorageConfigResponseModel | None = None
    deletionProtection: StrictBool | None = None
    controlPlaneScalingConfig: EKSControlPlaneScalingConfigModel | None = None
    kubeApiServerConfig: EKSKubeApiServerConfigResponseModel | None = None
    kubeSchedulerConfig: EKSKubeSchedulerConfigResponseModel | None = None
    kubeControllerManagerConfig: EKSKubeControllerManagerConfigResponseModel | None = None

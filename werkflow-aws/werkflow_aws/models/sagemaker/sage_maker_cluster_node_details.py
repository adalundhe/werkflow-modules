from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cluster_instance_placement import SageMakerClusterInstancePlacement
from .sage_maker_cluster_instance_status_details import SageMakerClusterInstanceStatusDetails
from .sage_maker_cluster_instance_storage_config import SageMakerClusterInstanceStorageConfig
from .sage_maker_cluster_kubernetes_config_node_details import SageMakerClusterKubernetesConfigNodeDetails
from .sage_maker_cluster_life_cycle_config import SageMakerClusterLifeCycleConfig
from .sage_maker_cluster_network_interface_details import SageMakerClusterNetworkInterfaceDetails
from .sage_maker_ultra_server_info import SageMakerUltraServerInfo
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerClusterNodeDetails(BaseModel):
    InstanceGroupName: StrictStr | None = None
    InstanceId: StrictStr | None = None
    NodeLogicalId: StrictStr | None = None
    InstanceStatus: SageMakerClusterInstanceStatusDetails | None = None
    InstanceType: StrictStr | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    LastSoftwareUpdateTime: datetime.datetime | StrictStr | None = None
    LifeCycleConfig: SageMakerClusterLifeCycleConfig | None = None
    OverrideVpcConfig: SageMakerVpcConfigModel | None = None
    ThreadsPerCore: StrictInt | None = None
    InstanceStorageConfigs: list[SageMakerClusterInstanceStorageConfig] | None = None
    PrivatePrimaryIp: StrictStr | None = None
    PrivatePrimaryIpv6: StrictStr | None = None
    PrivateDnsHostname: StrictStr | None = None
    Placement: SageMakerClusterInstancePlacement | None = None
    CurrentImageId: StrictStr | None = None
    DesiredImageId: StrictStr | None = None
    CurrentImageReleaseVersion: StrictStr | None = None
    DesiredImageReleaseVersion: StrictStr | None = None
    ImageVersionStatus: StrictStr | None = None
    UltraServerInfo: SageMakerUltraServerInfo | None = None
    KubernetesConfig: SageMakerClusterKubernetesConfigNodeDetails | None = None
    CapacityType: StrictStr | None = None
    NetworkInterface: SageMakerClusterNetworkInterfaceDetails | None = None

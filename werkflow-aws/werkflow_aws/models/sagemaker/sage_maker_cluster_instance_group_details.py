from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cluster_auto_patch_config_details import SageMakerClusterAutoPatchConfigDetails
from .sage_maker_cluster_capacity_requirements import SageMakerClusterCapacityRequirements
from .sage_maker_cluster_instance_requirement_details import SageMakerClusterInstanceRequirementDetails
from .sage_maker_cluster_instance_storage_config import SageMakerClusterInstanceStorageConfig
from .sage_maker_cluster_instance_type_detail import SageMakerClusterInstanceTypeDetail
from .sage_maker_cluster_kubernetes_config_details import SageMakerClusterKubernetesConfigDetails
from .sage_maker_cluster_life_cycle_config import SageMakerClusterLifeCycleConfig
from .sage_maker_cluster_network_interface_details import SageMakerClusterNetworkInterfaceDetails
from .sage_maker_cluster_slurm_config_details import SageMakerClusterSlurmConfigDetails
from .sage_maker_deployment_configuration import SageMakerDeploymentConfiguration
from .sage_maker_scheduled_update_config import SageMakerScheduledUpdateConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerClusterInstanceGroupDetails(BaseModel):
    CurrentCount: StrictInt | None = None
    TargetCount: StrictInt | None = None
    MinCount: StrictInt | None = None
    InstanceGroupName: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceRequirements: SageMakerClusterInstanceRequirementDetails | None = None
    InstanceTypeDetails: list[SageMakerClusterInstanceTypeDetail] | None = None
    LifeCycleConfig: SageMakerClusterLifeCycleConfig | None = None
    ExecutionRole: StrictStr | None = None
    ThreadsPerCore: StrictInt | None = None
    InstanceStorageConfigs: list[SageMakerClusterInstanceStorageConfig] | None = None
    OnStartDeepHealthChecks: list[StrictStr] | None = None
    Status: StrictStr | None = None
    TrainingPlanArn: StrictStr | None = None
    TrainingPlanStatus: StrictStr | None = None
    OverrideVpcConfig: SageMakerVpcConfigModel | None = None
    ScheduledUpdateConfig: SageMakerScheduledUpdateConfig | None = None
    AutoPatchConfig: SageMakerClusterAutoPatchConfigDetails | None = None
    CurrentImageId: StrictStr | None = None
    DesiredImageId: StrictStr | None = None
    CurrentImageReleaseVersion: StrictStr | None = None
    DesiredImageReleaseVersion: StrictStr | None = None
    ImageVersionStatus: StrictStr | None = None
    ActiveOperations: dict[StrictStr, StrictInt] | None = None
    KubernetesConfig: SageMakerClusterKubernetesConfigDetails | None = None
    CapacityRequirements: SageMakerClusterCapacityRequirements | None = None
    TargetStateCount: StrictInt | None = None
    SoftwareUpdateStatus: StrictStr | None = None
    ActiveSoftwareUpdateConfig: SageMakerDeploymentConfiguration | None = None
    SlurmConfig: SageMakerClusterSlurmConfigDetails | None = None
    NetworkInterface: SageMakerClusterNetworkInterfaceDetails | None = None

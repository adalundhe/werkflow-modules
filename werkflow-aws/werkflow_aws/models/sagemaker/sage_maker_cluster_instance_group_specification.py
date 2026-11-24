from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cluster_auto_patch_config import SageMakerClusterAutoPatchConfig
from .sage_maker_cluster_capacity_requirements import SageMakerClusterCapacityRequirements
from .sage_maker_cluster_instance_requirements import SageMakerClusterInstanceRequirements
from .sage_maker_cluster_instance_storage_config import SageMakerClusterInstanceStorageConfig
from .sage_maker_cluster_kubernetes_config import SageMakerClusterKubernetesConfig
from .sage_maker_cluster_life_cycle_config import SageMakerClusterLifeCycleConfig
from .sage_maker_cluster_network_interface import SageMakerClusterNetworkInterface
from .sage_maker_cluster_slurm_config import SageMakerClusterSlurmConfig
from .sage_maker_scheduled_update_config import SageMakerScheduledUpdateConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerClusterInstanceGroupSpecification(BaseModel):
    InstanceCount: StrictInt
    InstanceGroupName: StrictStr
    ExecutionRole: StrictStr
    MinInstanceCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    InstanceRequirements: SageMakerClusterInstanceRequirements | None = None
    LifeCycleConfig: SageMakerClusterLifeCycleConfig | None = None
    ThreadsPerCore: StrictInt | None = None
    InstanceStorageConfigs: list[SageMakerClusterInstanceStorageConfig] | None = None
    OnStartDeepHealthChecks: list[Literal['InstanceStress', 'InstanceConnectivity', 'MultiNodeTrainingValidation']] | None = None
    TrainingPlanArn: StrictStr | None = None
    OverrideVpcConfig: SageMakerVpcConfigModel | None = None
    ScheduledUpdateConfig: SageMakerScheduledUpdateConfig | None = None
    ImageId: StrictStr | None = None
    AutoPatchConfig: SageMakerClusterAutoPatchConfig | None = None
    ImageReleaseVersion: StrictStr | None = None
    KubernetesConfig: SageMakerClusterKubernetesConfig | None = None
    SlurmConfig: SageMakerClusterSlurmConfig | None = None
    CapacityRequirements: SageMakerClusterCapacityRequirements | None = None
    NetworkInterface: SageMakerClusterNetworkInterface | None = None

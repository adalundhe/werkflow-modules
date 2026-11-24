from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cluster_instance_storage_config import SageMakerClusterInstanceStorageConfig
from .sage_maker_environment_config import SageMakerEnvironmentConfig
from .sage_maker_scheduled_update_config import SageMakerScheduledUpdateConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerClusterRestrictedInstanceGroupSpecification(BaseModel):
    InstanceCount: StrictInt
    InstanceGroupName: StrictStr
    InstanceType: StrictStr
    ExecutionRole: StrictStr
    ThreadsPerCore: StrictInt | None = None
    InstanceStorageConfigs: list[SageMakerClusterInstanceStorageConfig] | None = None
    OnStartDeepHealthChecks: list[Literal['InstanceStress', 'InstanceConnectivity', 'MultiNodeTrainingValidation']] | None = None
    TrainingPlanArn: StrictStr | None = None
    OverrideVpcConfig: SageMakerVpcConfigModel | None = None
    ScheduledUpdateConfig: SageMakerScheduledUpdateConfig | None = None
    EnvironmentConfig: SageMakerEnvironmentConfig | None = None

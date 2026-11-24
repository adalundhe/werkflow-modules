from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cluster_instance_storage_config import SageMakerClusterInstanceStorageConfig
from .sage_maker_environment_config_details import SageMakerEnvironmentConfigDetails
from .sage_maker_scheduled_update_config import SageMakerScheduledUpdateConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerClusterRestrictedInstanceGroupDetails(BaseModel):
    CurrentCount: StrictInt | None = None
    TargetCount: StrictInt | None = None
    InstanceGroupName: StrictStr | None = None
    InstanceType: StrictStr | None = None
    ExecutionRole: StrictStr | None = None
    ThreadsPerCore: StrictInt | None = None
    InstanceStorageConfigs: list[SageMakerClusterInstanceStorageConfig] | None = None
    OnStartDeepHealthChecks: list[StrictStr] | None = None
    Status: StrictStr | None = None
    TrainingPlanArn: StrictStr | None = None
    TrainingPlanStatus: StrictStr | None = None
    OverrideVpcConfig: SageMakerVpcConfigModel | None = None
    ScheduledUpdateConfig: SageMakerScheduledUpdateConfig | None = None
    EnvironmentConfig: SageMakerEnvironmentConfigDetails | None = None

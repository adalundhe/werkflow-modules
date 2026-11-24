from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_auto_scaling_group_provider_update import ECSAutoScalingGroupProviderUpdate
from .ecs_update_managed_instances_provider_configuration import ECSUpdateManagedInstancesProviderConfiguration


class ECSUpdateCapacityProviderRequest(BaseModel):
    name: StrictStr
    cluster: StrictStr | None = None
    autoScalingGroupProvider: ECSAutoScalingGroupProviderUpdate | None = None
    managedInstancesProvider: ECSUpdateManagedInstancesProviderConfiguration | None = None

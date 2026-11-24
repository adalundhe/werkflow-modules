from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_auto_scaling_group_provider import ECSAutoScalingGroupProvider
from .ecs_create_managed_instances_provider_configuration import ECSCreateManagedInstancesProviderConfiguration
from .ecs_tag import ECSTag


class ECSCreateCapacityProviderRequest(BaseModel):
    name: StrictStr
    cluster: StrictStr | None = None
    autoScalingGroupProvider: ECSAutoScalingGroupProvider | None = None
    managedInstancesProvider: ECSCreateManagedInstancesProviderConfiguration | None = None
    tags: list[ECSTag] | None = None

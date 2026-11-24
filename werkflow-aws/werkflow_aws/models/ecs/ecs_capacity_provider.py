from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_auto_scaling_group_provider import ECSAutoScalingGroupProvider
from .ecs_managed_instances_provider import ECSManagedInstancesProvider
from .ecs_tag import ECSTag


class ECSCapacityProvider(BaseModel):
    capacityProviderArn: StrictStr | None = None
    name: StrictStr | None = None
    cluster: StrictStr | None = None
    status: StrictStr | None = None
    autoScalingGroupProvider: ECSAutoScalingGroupProvider | None = None
    managedInstancesProvider: ECSManagedInstancesProvider | None = None
    updateStatus: StrictStr | None = None
    updateStatusReason: StrictStr | None = None
    tags: list[ECSTag] | None = None
    type: StrictStr | None = None

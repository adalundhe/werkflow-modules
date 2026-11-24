from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_consumable_resource_properties import BatchConsumableResourceProperties
from .batch_container_overrides import BatchContainerOverrides
from .batch_ecs_properties_override import BatchEcsPropertiesOverride
from .batch_eks_properties_override import BatchEksPropertiesOverride


class BatchNodePropertyOverride(BaseModel):
    targetNodes: StrictStr
    containerOverrides: BatchContainerOverrides | None = None
    ecsPropertiesOverride: BatchEcsPropertiesOverride | None = None
    instanceTypes: list[StrictStr] | None = None
    eksPropertiesOverride: BatchEksPropertiesOverride | None = None
    consumableResourcePropertiesOverride: BatchConsumableResourceProperties | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_consumable_resource_properties import BatchConsumableResourceProperties
from .batch_container_properties import BatchContainerProperties
from .batch_ecs_properties import BatchEcsProperties
from .batch_eks_properties import BatchEksProperties


class BatchNodeRangeProperty(BaseModel):
    targetNodes: StrictStr | None = None
    container: BatchContainerProperties | None = None
    instanceTypes: list[StrictStr] | None = None
    ecsProperties: BatchEcsProperties | None = None
    eksProperties: BatchEksProperties | None = None
    consumableResourceProperties: BatchConsumableResourceProperties | None = None

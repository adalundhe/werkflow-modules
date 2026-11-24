from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_consumable_resource_properties import BatchConsumableResourceProperties
from .batch_container_properties import BatchContainerProperties
from .batch_ecs_properties import BatchEcsProperties
from .batch_eks_properties import BatchEksProperties
from .batch_job_timeout import BatchJobTimeout
from .batch_node_properties import BatchNodeProperties
from .batch_retry_strategy import BatchRetryStrategy


class BatchJobDefinition(BaseModel):
    jobDefinitionName: StrictStr | None = None
    jobDefinitionArn: StrictStr | None = None
    revision: StrictInt | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    schedulingPriority: StrictInt | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    retryStrategy: BatchRetryStrategy | None = None
    containerProperties: BatchContainerProperties | None = None
    timeout: BatchJobTimeout | None = None
    nodeProperties: BatchNodeProperties | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    propagateTags: StrictBool | None = None
    platformCapabilities: list[StrictStr] | None = None
    ecsProperties: BatchEcsProperties | None = None
    eksProperties: BatchEksProperties | None = None
    containerOrchestrationType: StrictStr | None = None
    consumableResourceProperties: BatchConsumableResourceProperties | None = None

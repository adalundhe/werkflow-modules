from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_consumable_resource_properties import BatchConsumableResourceProperties
from .batch_container_properties import BatchContainerProperties
from .batch_ecs_properties import BatchEcsProperties
from .batch_eks_properties import BatchEksProperties
from .batch_job_timeout import BatchJobTimeout
from .batch_node_properties import BatchNodeProperties
from .batch_retry_strategy import BatchRetryStrategy


class BatchRegisterJobDefinitionRequest(BaseModel):
    jobDefinitionName: StrictStr
    type: Literal['container', 'multinode']
    parameters: dict[StrictStr, StrictStr] | None = None
    schedulingPriority: StrictInt | None = None
    containerProperties: BatchContainerProperties | None = None
    nodeProperties: BatchNodeProperties | None = None
    retryStrategy: BatchRetryStrategy | None = None
    propagateTags: StrictBool | None = None
    timeout: BatchJobTimeout | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    platformCapabilities: list[Literal['EC2', 'FARGATE', 'MANAGED_INSTANCES']] | None = None
    eksProperties: BatchEksProperties | None = None
    ecsProperties: BatchEcsProperties | None = None
    consumableResourceProperties: BatchConsumableResourceProperties | None = None

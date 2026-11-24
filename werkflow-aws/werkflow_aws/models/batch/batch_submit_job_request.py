from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_array_properties import BatchArrayProperties
from .batch_consumable_resource_properties import BatchConsumableResourceProperties
from .batch_container_overrides import BatchContainerOverrides
from .batch_ecs_properties_override import BatchEcsPropertiesOverride
from .batch_eks_properties_override import BatchEksPropertiesOverride
from .batch_job_dependency import BatchJobDependency
from .batch_job_timeout import BatchJobTimeout
from .batch_node_overrides import BatchNodeOverrides
from .batch_retry_strategy import BatchRetryStrategy


class BatchSubmitJobRequest(BaseModel):
    jobName: StrictStr
    jobQueue: StrictStr
    jobDefinition: StrictStr
    shareIdentifier: StrictStr | None = None
    schedulingPriorityOverride: StrictInt | None = None
    arrayProperties: BatchArrayProperties | None = None
    dependsOn: list[BatchJobDependency] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    containerOverrides: BatchContainerOverrides | None = None
    nodeOverrides: BatchNodeOverrides | None = None
    retryStrategy: BatchRetryStrategy | None = None
    propagateTags: StrictBool | None = None
    timeout: BatchJobTimeout | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    eksPropertiesOverride: BatchEksPropertiesOverride | None = None
    ecsPropertiesOverride: BatchEcsPropertiesOverride | None = None
    consumableResourcePropertiesOverride: BatchConsumableResourceProperties | None = None

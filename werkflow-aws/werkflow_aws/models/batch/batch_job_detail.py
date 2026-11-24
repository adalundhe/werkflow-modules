from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_array_properties_detail import BatchArrayPropertiesDetail
from .batch_attempt_detail import BatchAttemptDetail
from .batch_consumable_resource_properties import BatchConsumableResourceProperties
from .batch_container_detail import BatchContainerDetail
from .batch_ecs_properties_detail import BatchEcsPropertiesDetail
from .batch_eks_attempt_detail import BatchEksAttemptDetail
from .batch_eks_properties_detail import BatchEksPropertiesDetail
from .batch_job_dependency import BatchJobDependency
from .batch_job_timeout import BatchJobTimeout
from .batch_node_details import BatchNodeDetails
from .batch_node_properties import BatchNodeProperties
from .batch_retry_strategy import BatchRetryStrategy


class BatchJobDetail(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    jobId: StrictStr | None = None
    jobQueue: StrictStr | None = None
    status: StrictStr | None = None
    shareIdentifier: StrictStr | None = None
    schedulingPriority: StrictInt | None = None
    attempts: list[BatchAttemptDetail] | None = None
    statusReason: StrictStr | None = None
    createdAt: StrictInt | None = None
    retryStrategy: BatchRetryStrategy | None = None
    startedAt: StrictInt | None = None
    stoppedAt: StrictInt | None = None
    dependsOn: list[BatchJobDependency] | None = None
    jobDefinition: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    container: BatchContainerDetail | None = None
    nodeDetails: BatchNodeDetails | None = None
    nodeProperties: BatchNodeProperties | None = None
    arrayProperties: BatchArrayPropertiesDetail | None = None
    timeout: BatchJobTimeout | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    propagateTags: StrictBool | None = None
    platformCapabilities: list[StrictStr] | None = None
    eksProperties: BatchEksPropertiesDetail | None = None
    eksAttempts: list[BatchEksAttemptDetail] | None = None
    ecsProperties: BatchEcsPropertiesDetail | None = None
    isCancelled: StrictBool | None = None
    isTerminated: StrictBool | None = None
    consumableResourceProperties: BatchConsumableResourceProperties | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_array_properties_summary import BatchArrayPropertiesSummary
from .batch_container_summary import BatchContainerSummary
from .batch_job_capacity_usage_summary import BatchJobCapacityUsageSummary
from .batch_node_properties_summary import BatchNodePropertiesSummary


class BatchJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    jobName: StrictStr | None = None
    capacityUsage: list[BatchJobCapacityUsageSummary] | None = None
    createdAt: StrictInt | None = None
    scheduledAt: StrictInt | None = None
    shareIdentifier: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    startedAt: StrictInt | None = None
    stoppedAt: StrictInt | None = None
    container: BatchContainerSummary | None = None
    arrayProperties: BatchArrayPropertiesSummary | None = None
    nodeProperties: BatchNodePropertiesSummary | None = None
    jobDefinition: StrictStr | None = None
    isCancelled: StrictBool | None = None
    isTerminated: StrictBool | None = None

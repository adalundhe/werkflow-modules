from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_latest_service_job_attempt import BatchLatestServiceJobAttempt
from .batch_service_job_capacity_usage_summary import BatchServiceJobCapacityUsageSummary


class BatchServiceJobSummary(BaseModel):
    latestAttempt: BatchLatestServiceJobAttempt | None = None
    capacityUsage: list[BatchServiceJobCapacityUsageSummary] | None = None
    createdAt: StrictInt | None = None
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    jobName: StrictStr | None = None
    scheduledAt: StrictInt | None = None
    serviceJobType: StrictStr | None = None
    shareIdentifier: StrictStr | None = None
    quotaShareName: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    startedAt: StrictInt | None = None
    stoppedAt: StrictInt | None = None
    isTerminated: StrictBool | None = None

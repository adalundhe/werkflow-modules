from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_latest_service_job_attempt import BatchLatestServiceJobAttempt
from .batch_service_job_attempt_detail import BatchServiceJobAttemptDetail
from .batch_service_job_capacity_usage_detail import BatchServiceJobCapacityUsageDetail
from .batch_service_job_preemption_configuration import BatchServiceJobPreemptionConfiguration
from .batch_service_job_preemption_summary import BatchServiceJobPreemptionSummary
from .batch_service_job_retry_strategy import BatchServiceJobRetryStrategy
from .batch_service_job_timeout import BatchServiceJobTimeout


class BatchDescribeServiceJobResponse(BaseModel):
    attempts: list[BatchServiceJobAttemptDetail] | None = None
    capacityUsage: list[BatchServiceJobCapacityUsageDetail] | None = None
    createdAt: StrictInt | None = None
    isTerminated: StrictBool | None = None
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    jobName: StrictStr | None = None
    jobQueue: StrictStr | None = None
    latestAttempt: BatchLatestServiceJobAttempt | None = None
    retryStrategy: BatchServiceJobRetryStrategy | None = None
    scheduledAt: StrictInt | None = None
    schedulingPriority: StrictInt | None = None
    serviceRequestPayload: StrictStr | None = None
    serviceJobType: StrictStr | None = None
    shareIdentifier: StrictStr | None = None
    quotaShareName: StrictStr | None = None
    preemptionConfiguration: BatchServiceJobPreemptionConfiguration | None = None
    preemptionSummary: BatchServiceJobPreemptionSummary | None = None
    startedAt: StrictInt | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    stoppedAt: StrictInt | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    timeoutConfig: BatchServiceJobTimeout | None = None
    ResponseMetadata: dict[str, Any] | None = None

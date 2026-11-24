from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_service_job_preemption_configuration import BatchServiceJobPreemptionConfiguration
from .batch_service_job_retry_strategy import BatchServiceJobRetryStrategy
from .batch_service_job_timeout import BatchServiceJobTimeout


class BatchSubmitServiceJobRequest(BaseModel):
    jobName: StrictStr
    jobQueue: StrictStr
    serviceRequestPayload: StrictStr
    serviceJobType: Literal['SAGEMAKER_TRAINING']
    retryStrategy: BatchServiceJobRetryStrategy | None = None
    schedulingPriority: StrictInt | None = None
    shareIdentifier: StrictStr | None = None
    quotaShareName: StrictStr | None = None
    preemptionConfiguration: BatchServiceJobPreemptionConfiguration | None = None
    timeoutConfig: BatchServiceJobTimeout | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    clientToken: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_environment_order import BatchComputeEnvironmentOrder
from .batch_job_state_time_limit_action import BatchJobStateTimeLimitAction
from .batch_service_environment_order import BatchServiceEnvironmentOrder


class BatchJobQueueDetail(BaseModel):
    jobQueueName: StrictStr | None = None
    jobQueueArn: StrictStr | None = None
    state: StrictStr | None = None
    schedulingPolicyArn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    priority: StrictInt | None = None
    computeEnvironmentOrder: list[BatchComputeEnvironmentOrder] | None = None
    serviceEnvironmentOrder: list[BatchServiceEnvironmentOrder] | None = None
    jobQueueType: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    jobStateTimeLimitActions: list[BatchJobStateTimeLimitAction] | None = None

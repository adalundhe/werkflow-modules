from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_environment_order import BatchComputeEnvironmentOrder
from .batch_job_state_time_limit_action import BatchJobStateTimeLimitAction
from .batch_service_environment_order import BatchServiceEnvironmentOrder


class BatchUpdateJobQueueRequest(BaseModel):
    jobQueue: StrictStr
    state: Literal['ENABLED', 'DISABLED'] | None = None
    schedulingPolicyArn: StrictStr | None = None
    priority: StrictInt | None = None
    computeEnvironmentOrder: list[BatchComputeEnvironmentOrder] | None = None
    serviceEnvironmentOrder: list[BatchServiceEnvironmentOrder] | None = None
    jobStateTimeLimitActions: list[BatchJobStateTimeLimitAction] | None = None

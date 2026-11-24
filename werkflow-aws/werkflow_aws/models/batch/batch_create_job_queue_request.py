from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_environment_order import BatchComputeEnvironmentOrder
from .batch_job_state_time_limit_action import BatchJobStateTimeLimitAction
from .batch_service_environment_order import BatchServiceEnvironmentOrder


class BatchCreateJobQueueRequest(BaseModel):
    jobQueueName: StrictStr
    priority: StrictInt
    state: Literal['ENABLED', 'DISABLED'] | None = None
    schedulingPolicyArn: StrictStr | None = None
    computeEnvironmentOrder: list[BatchComputeEnvironmentOrder] | None = None
    serviceEnvironmentOrder: list[BatchServiceEnvironmentOrder] | None = None
    jobQueueType: Literal['EKS', 'ECS', 'ECS_FARGATE', 'SAGEMAKER_TRAINING', 'ECS_MANAGED_INSTANCES'] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    jobStateTimeLimitActions: list[BatchJobStateTimeLimitAction] | None = None

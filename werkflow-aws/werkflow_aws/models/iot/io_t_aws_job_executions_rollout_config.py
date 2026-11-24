from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .io_t_aws_job_exponential_rollout_rate import IoTAwsJobExponentialRolloutRate


class IoTAwsJobExecutionsRolloutConfig(BaseModel):
    maximumPerMinute: StrictInt | None = None
    exponentialRate: IoTAwsJobExponentialRolloutRate | None = None

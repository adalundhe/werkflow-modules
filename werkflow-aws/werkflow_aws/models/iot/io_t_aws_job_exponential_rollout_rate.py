from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .io_t_aws_job_rate_increase_criteria import IoTAwsJobRateIncreaseCriteria


class IoTAwsJobExponentialRolloutRate(BaseModel):
    baseRatePerMinute: StrictInt | None = None
    incrementFactor: StrictFloat | StrictInt | None = None
    rateIncreaseCriteria: IoTAwsJobRateIncreaseCriteria | None = None

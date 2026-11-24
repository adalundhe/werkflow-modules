from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .io_t_exponential_rollout_rate import IoTExponentialRolloutRate


class IoTJobExecutionsRolloutConfig(BaseModel):
    maximumPerMinute: StrictInt | None = None
    exponentialRate: IoTExponentialRolloutRate | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .io_t_rate_increase_criteria import IoTRateIncreaseCriteria


class IoTExponentialRolloutRate(BaseModel):
    baseRatePerMinute: StrictInt | None = None
    incrementFactor: StrictFloat | StrictInt | None = None
    rateIncreaseCriteria: IoTRateIncreaseCriteria | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTAwsJobRateIncreaseCriteria(BaseModel):
    numberOfNotifiedThings: StrictInt | None = None
    numberOfSucceededThings: StrictInt | None = None

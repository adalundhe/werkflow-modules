from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTRateIncreaseCriteria(BaseModel):
    numberOfNotifiedThings: StrictInt | None = None
    numberOfSucceededThings: StrictInt | None = None

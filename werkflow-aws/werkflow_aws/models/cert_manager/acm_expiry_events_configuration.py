from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ACMExpiryEventsConfiguration(BaseModel):
    DaysBeforeExpiry: StrictInt | None = None

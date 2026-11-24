from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3EventHoldDuration(BaseModel):
    Days: StrictInt | None = None
    Years: StrictInt | None = None

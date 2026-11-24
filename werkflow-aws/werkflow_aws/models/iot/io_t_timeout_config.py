from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTTimeoutConfig(BaseModel):
    inProgressTimeoutInMinutes: StrictInt | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTAwsJobTimeoutConfig(BaseModel):
    inProgressTimeoutInMinutes: StrictInt | None = None

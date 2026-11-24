from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTAwsJobPresignedUrlConfig(BaseModel):
    expiresInSec: StrictInt | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTPresignedUrlConfig(BaseModel):
    roleArn: StrictStr | None = None
    expiresInSec: StrictInt | None = None

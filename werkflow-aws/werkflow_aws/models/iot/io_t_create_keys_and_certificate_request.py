from __future__ import annotations
from pydantic import BaseModel, StrictBool


class IoTCreateKeysAndCertificateRequest(BaseModel):
    setAsActive: StrictBool | None = None

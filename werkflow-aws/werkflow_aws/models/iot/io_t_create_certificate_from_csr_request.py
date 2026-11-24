from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCreateCertificateFromCsrRequest(BaseModel):
    certificateSigningRequest: StrictStr
    setAsActive: StrictBool | None = None

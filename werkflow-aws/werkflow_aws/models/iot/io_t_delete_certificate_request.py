from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTDeleteCertificateRequest(BaseModel):
    certificateId: StrictStr
    forceDelete: StrictBool | None = None

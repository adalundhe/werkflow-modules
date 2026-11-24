from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAcceptCertificateTransferRequest(BaseModel):
    certificateId: StrictStr
    setAsActive: StrictBool | None = None

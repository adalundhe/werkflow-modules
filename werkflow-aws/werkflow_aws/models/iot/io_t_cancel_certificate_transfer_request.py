from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCancelCertificateTransferRequest(BaseModel):
    certificateId: StrictStr

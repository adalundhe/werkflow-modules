from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTRejectCertificateTransferRequest(BaseModel):
    certificateId: StrictStr
    rejectReason: StrictStr | None = None

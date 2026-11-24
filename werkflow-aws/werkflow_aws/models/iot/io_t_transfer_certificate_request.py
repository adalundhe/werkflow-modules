from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTTransferCertificateRequest(BaseModel):
    certificateId: StrictStr
    targetAwsAccount: StrictStr
    transferMessage: StrictStr | None = None

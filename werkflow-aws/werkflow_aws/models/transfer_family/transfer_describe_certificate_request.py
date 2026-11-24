from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeCertificateRequest(BaseModel):
    CertificateId: StrictStr

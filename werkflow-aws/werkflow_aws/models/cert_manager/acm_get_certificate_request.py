from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMGetCertificateRequest(BaseModel):
    CertificateArn: StrictStr

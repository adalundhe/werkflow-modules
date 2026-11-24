from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDescribeCertificateRequest(BaseModel):
    CertificateArn: StrictStr

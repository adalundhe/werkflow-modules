from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteCertificateRequest(BaseModel):
    CertificateArn: StrictStr

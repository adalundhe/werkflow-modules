from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetServerCertificateRequest(BaseModel):
    ServerCertificateName: StrictStr

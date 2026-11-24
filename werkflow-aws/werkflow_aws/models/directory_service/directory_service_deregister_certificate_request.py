from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDeregisterCertificateRequest(BaseModel):
    DirectoryId: StrictStr
    CertificateId: StrictStr

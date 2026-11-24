from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeCertificateRequest(BaseModel):
    DirectoryId: StrictStr
    CertificateId: StrictStr

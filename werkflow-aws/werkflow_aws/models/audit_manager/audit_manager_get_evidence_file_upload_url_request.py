from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerGetEvidenceFileUploadUrlRequest(BaseModel):
    fileName: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerGetEvidenceRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    evidenceFolderId: StrictStr
    evidenceId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerGetEvidenceFolderRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    evidenceFolderId: StrictStr

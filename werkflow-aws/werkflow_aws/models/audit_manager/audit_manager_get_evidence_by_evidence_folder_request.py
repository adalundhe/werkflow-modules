from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerGetEvidenceByEvidenceFolderRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    evidenceFolderId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

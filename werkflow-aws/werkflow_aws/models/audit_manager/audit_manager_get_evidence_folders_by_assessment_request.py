from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerGetEvidenceFoldersByAssessmentRequest(BaseModel):
    assessmentId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

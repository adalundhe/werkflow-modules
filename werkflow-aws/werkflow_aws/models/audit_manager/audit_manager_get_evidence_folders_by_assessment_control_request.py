from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerGetEvidenceFoldersByAssessmentControlRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    controlId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

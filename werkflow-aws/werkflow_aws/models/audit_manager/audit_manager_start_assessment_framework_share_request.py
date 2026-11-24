from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerStartAssessmentFrameworkShareRequest(BaseModel):
    frameworkId: StrictStr
    destinationAccount: StrictStr
    destinationRegion: StrictStr
    comment: StrictStr | None = None

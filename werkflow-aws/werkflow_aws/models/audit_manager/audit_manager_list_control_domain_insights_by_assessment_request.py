from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListControlDomainInsightsByAssessmentRequest(BaseModel):
    assessmentId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

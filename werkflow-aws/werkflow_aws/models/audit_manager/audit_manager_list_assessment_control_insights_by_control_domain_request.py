from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListAssessmentControlInsightsByControlDomainRequest(BaseModel):
    controlDomainId: StrictStr
    assessmentId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

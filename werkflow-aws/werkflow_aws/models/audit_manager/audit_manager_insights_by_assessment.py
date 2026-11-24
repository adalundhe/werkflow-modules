from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerInsightsByAssessment(BaseModel):
    noncompliantEvidenceCount: StrictInt | None = None
    compliantEvidenceCount: StrictInt | None = None
    inconclusiveEvidenceCount: StrictInt | None = None
    assessmentControlsCountByNoncompliantEvidence: StrictInt | None = None
    totalAssessmentControlsCount: StrictInt | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None

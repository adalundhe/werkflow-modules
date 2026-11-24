from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerInsights(BaseModel):
    activeAssessmentsCount: StrictInt | None = None
    noncompliantEvidenceCount: StrictInt | None = None
    compliantEvidenceCount: StrictInt | None = None
    inconclusiveEvidenceCount: StrictInt | None = None
    assessmentControlsCountByNoncompliantEvidence: StrictInt | None = None
    totalAssessmentControlsCount: StrictInt | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None

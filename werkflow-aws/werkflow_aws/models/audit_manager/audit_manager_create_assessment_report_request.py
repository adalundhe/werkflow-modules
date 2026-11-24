from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerCreateAssessmentReportRequest(BaseModel):
    name: StrictStr
    assessmentId: StrictStr
    description: StrictStr | None = None
    queryStatement: StrictStr | None = None

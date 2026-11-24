from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDeleteAssessmentReportRequest(BaseModel):
    assessmentId: StrictStr
    assessmentReportId: StrictStr

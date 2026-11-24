from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerGetInsightsByAssessmentRequest(BaseModel):
    assessmentId: StrictStr

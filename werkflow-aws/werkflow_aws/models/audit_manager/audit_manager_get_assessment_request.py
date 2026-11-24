from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerGetAssessmentRequest(BaseModel):
    assessmentId: StrictStr

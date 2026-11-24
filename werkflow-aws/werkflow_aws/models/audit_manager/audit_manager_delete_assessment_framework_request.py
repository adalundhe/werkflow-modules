from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDeleteAssessmentFrameworkRequest(BaseModel):
    frameworkId: StrictStr

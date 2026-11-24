from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerValidateAssessmentReportIntegrityRequest(BaseModel):
    s3RelativePath: StrictStr

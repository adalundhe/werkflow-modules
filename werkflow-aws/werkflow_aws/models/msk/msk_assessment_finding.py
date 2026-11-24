from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_finding_remediation import MSKFindingRemediation


class MSKAssessmentFinding(BaseModel):
    Category: StrictStr | None = None
    FindingId: StrictStr | None = None
    Message: StrictStr | None = None
    Remediation: MSKFindingRemediation | None = None
    Resource: StrictStr | None = None
    Severity: StrictStr | None = None

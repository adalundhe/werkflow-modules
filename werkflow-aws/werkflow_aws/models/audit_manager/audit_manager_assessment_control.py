from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .audit_manager_control_comment import AuditManagerControlComment


class AuditManagerAssessmentControl(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    response: StrictStr | None = None
    comments: list[AuditManagerControlComment] | None = None
    evidenceSources: list[StrictStr] | None = None
    evidenceCount: StrictInt | None = None
    assessmentReportEvidenceCount: StrictInt | None = None

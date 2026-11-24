from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_create_assessment_framework_control import AuditManagerCreateAssessmentFrameworkControl


class AuditManagerUpdateAssessmentFrameworkControlSet(BaseModel):
    name: StrictStr
    controls: list[AuditManagerCreateAssessmentFrameworkControl]
    id: StrictStr | None = None

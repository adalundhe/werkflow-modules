from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_create_assessment_framework_control_set import AuditManagerCreateAssessmentFrameworkControlSet


class AuditManagerCreateAssessmentFrameworkRequest(BaseModel):
    name: StrictStr
    controlSets: list[AuditManagerCreateAssessmentFrameworkControlSet]
    description: StrictStr | None = None
    complianceType: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None

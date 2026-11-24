from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_update_assessment_framework_control_set import AuditManagerUpdateAssessmentFrameworkControlSet


class AuditManagerUpdateAssessmentFrameworkRequest(BaseModel):
    frameworkId: StrictStr
    name: StrictStr
    controlSets: list[AuditManagerUpdateAssessmentFrameworkControlSet]
    description: StrictStr | None = None
    complianceType: StrictStr | None = None

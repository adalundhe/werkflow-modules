from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_reports_destination import AuditManagerAssessmentReportsDestination
from .audit_manager_role import AuditManagerRole
from .audit_manager_scope import AuditManagerScope


class AuditManagerCreateAssessmentRequest(BaseModel):
    name: StrictStr
    assessmentReportsDestination: AuditManagerAssessmentReportsDestination
    scope: AuditManagerScope
    roles: list[AuditManagerRole]
    frameworkId: StrictStr
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None

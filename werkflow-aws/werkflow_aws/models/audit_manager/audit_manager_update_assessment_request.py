from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_reports_destination import AuditManagerAssessmentReportsDestination
from .audit_manager_role import AuditManagerRole
from .audit_manager_scope import AuditManagerScope


class AuditManagerUpdateAssessmentRequest(BaseModel):
    assessmentId: StrictStr
    scope: AuditManagerScope
    assessmentName: StrictStr | None = None
    assessmentDescription: StrictStr | None = None
    assessmentReportsDestination: AuditManagerAssessmentReportsDestination | None = None
    roles: list[AuditManagerRole] | None = None

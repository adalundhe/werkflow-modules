from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_reports_destination import AuditManagerAssessmentReportsDestination
from .audit_manager_delegation import AuditManagerDelegation
from .audit_manager_role import AuditManagerRole
from .audit_manager_scope import AuditManagerScope


class AuditManagerAssessmentMetadata(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
    description: StrictStr | None = None
    complianceType: StrictStr | None = None
    status: StrictStr | None = None
    assessmentReportsDestination: AuditManagerAssessmentReportsDestination | None = None
    scope: AuditManagerScope | None = None
    roles: list[AuditManagerRole] | None = None
    delegations: list[AuditManagerDelegation] | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .audit_manager_assessment_control import AuditManagerAssessmentControl
from .audit_manager_delegation import AuditManagerDelegation
from .audit_manager_role import AuditManagerRole


class AuditManagerAssessmentControlSet(BaseModel):
    id: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    roles: list[AuditManagerRole] | None = None
    controls: list[AuditManagerAssessmentControl] | None = None
    delegations: list[AuditManagerDelegation] | None = None
    systemEvidenceCount: StrictInt | None = None
    manualEvidenceCount: StrictInt | None = None

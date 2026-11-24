from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .audit_manager_delegation import AuditManagerDelegation
from .audit_manager_role import AuditManagerRole


class AuditManagerAssessmentMetadataItem(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
    complianceType: StrictStr | None = None
    status: StrictStr | None = None
    roles: list[AuditManagerRole] | None = None
    delegations: list[AuditManagerDelegation] | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None

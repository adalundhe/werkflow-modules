from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .audit_manager_control_set import AuditManagerControlSet


class AuditManagerFramework(BaseModel):
    arn: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    complianceType: StrictStr | None = None
    description: StrictStr | None = None
    logo: StrictStr | None = None
    controlSources: StrictStr | None = None
    controlSets: list[AuditManagerControlSet] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None

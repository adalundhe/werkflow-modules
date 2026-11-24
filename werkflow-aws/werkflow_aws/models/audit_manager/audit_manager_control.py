from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .audit_manager_control_mapping_source import AuditManagerControlMappingSource


class AuditManagerControl(BaseModel):
    arn: StrictStr | None = None
    id: StrictStr | None = None
    type: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    testingInformation: StrictStr | None = None
    actionPlanTitle: StrictStr | None = None
    actionPlanInstructions: StrictStr | None = None
    controlSources: StrictStr | None = None
    controlMappingSources: list[AuditManagerControlMappingSource] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    state: StrictStr | None = None

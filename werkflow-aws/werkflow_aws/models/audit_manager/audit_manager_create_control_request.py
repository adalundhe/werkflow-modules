from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_create_control_mapping_source import AuditManagerCreateControlMappingSource


class AuditManagerCreateControlRequest(BaseModel):
    name: StrictStr
    controlMappingSources: list[AuditManagerCreateControlMappingSource]
    description: StrictStr | None = None
    testingInformation: StrictStr | None = None
    actionPlanTitle: StrictStr | None = None
    actionPlanInstructions: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None

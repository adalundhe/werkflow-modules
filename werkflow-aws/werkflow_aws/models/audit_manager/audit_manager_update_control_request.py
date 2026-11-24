from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_control_mapping_source import AuditManagerControlMappingSource


class AuditManagerUpdateControlRequest(BaseModel):
    controlId: StrictStr
    name: StrictStr
    controlMappingSources: list[AuditManagerControlMappingSource]
    description: StrictStr | None = None
    testingInformation: StrictStr | None = None
    actionPlanTitle: StrictStr | None = None
    actionPlanInstructions: StrictStr | None = None

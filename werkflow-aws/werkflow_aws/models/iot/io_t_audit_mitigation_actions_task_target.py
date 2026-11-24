from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAuditMitigationActionsTaskTarget(BaseModel):
    auditTaskId: StrictStr | None = None
    findingIds: list[StrictStr] | None = None
    auditCheckToReasonCodeFilter: dict[StrictStr, list[StrictStr]] | None = None

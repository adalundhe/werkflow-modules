from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_mitigation_actions_task_metadata import IoTAuditMitigationActionsTaskMetadata


class IoTListAuditMitigationActionsTasksResponse(BaseModel):
    tasks: list[IoTAuditMitigationActionsTaskMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

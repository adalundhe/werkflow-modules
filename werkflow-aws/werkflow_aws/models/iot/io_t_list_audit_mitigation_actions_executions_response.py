from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_mitigation_action_execution_metadata import IoTAuditMitigationActionExecutionMetadata


class IoTListAuditMitigationActionsExecutionsResponse(BaseModel):
    actionsExecutions: list[IoTAuditMitigationActionExecutionMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

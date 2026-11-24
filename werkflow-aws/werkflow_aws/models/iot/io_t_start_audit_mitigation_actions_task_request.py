from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_audit_mitigation_actions_task_target import IoTAuditMitigationActionsTaskTarget


class IoTStartAuditMitigationActionsTaskRequest(BaseModel):
    taskId: StrictStr
    target: IoTAuditMitigationActionsTaskTarget
    auditCheckToActionsMapping: dict[StrictStr, list[StrictStr]]
    clientRequestToken: StrictStr

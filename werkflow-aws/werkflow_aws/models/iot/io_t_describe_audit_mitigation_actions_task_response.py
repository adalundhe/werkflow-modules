from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_mitigation_actions_task_target import IoTAuditMitigationActionsTaskTarget
from .io_t_mitigation_action import IoTMitigationAction
from .io_t_task_statistics_for_audit_check import IoTTaskStatisticsForAuditCheck


class IoTDescribeAuditMitigationActionsTaskResponse(BaseModel):
    taskStatus: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    taskStatistics: dict[StrictStr, IoTTaskStatisticsForAuditCheck] | None = None
    target: IoTAuditMitigationActionsTaskTarget | None = None
    auditCheckToActionsMapping: dict[StrictStr, list[StrictStr]] | None = None
    actionsDefinition: list[IoTMitigationAction] | None = None
    ResponseMetadata: dict[str, Any] | None = None

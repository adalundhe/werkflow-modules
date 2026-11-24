from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_check_details import IoTAuditCheckDetails
from .io_t_task_statistics import IoTTaskStatistics


class IoTDescribeAuditTaskResponse(BaseModel):
    taskStatus: StrictStr | None = None
    taskType: StrictStr | None = None
    taskStartTime: datetime.datetime | StrictStr | None = None
    taskStatistics: IoTTaskStatistics | None = None
    scheduledAuditName: StrictStr | None = None
    auditDetails: dict[StrictStr, IoTAuditCheckDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None

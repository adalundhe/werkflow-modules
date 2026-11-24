from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_scheduled_window_execution import SSMScheduledWindowExecution


class SSMDescribeMaintenanceWindowScheduleResponse(BaseModel):
    ScheduledWindowExecutions: list[SSMScheduledWindowExecution] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

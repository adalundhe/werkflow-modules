from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_maintenance_window_execution import SSMMaintenanceWindowExecution


class SSMDescribeMaintenanceWindowExecutionsResponse(BaseModel):
    WindowExecutions: list[SSMMaintenanceWindowExecution] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

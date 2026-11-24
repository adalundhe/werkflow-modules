from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_maintenance_window_task import SSMMaintenanceWindowTask


class SSMDescribeMaintenanceWindowTasksResponse(BaseModel):
    Tasks: list[SSMMaintenanceWindowTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

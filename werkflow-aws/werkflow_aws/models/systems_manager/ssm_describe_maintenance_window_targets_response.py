from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_maintenance_window_target import SSMMaintenanceWindowTarget


class SSMDescribeMaintenanceWindowTargetsResponse(BaseModel):
    Targets: list[SSMMaintenanceWindowTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

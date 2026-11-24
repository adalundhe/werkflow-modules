from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_maintenance_window_identity import SSMMaintenanceWindowIdentity


class SSMDescribeMaintenanceWindowsResponse(BaseModel):
    WindowIdentities: list[SSMMaintenanceWindowIdentity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

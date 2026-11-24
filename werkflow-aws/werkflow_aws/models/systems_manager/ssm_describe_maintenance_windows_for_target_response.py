from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_maintenance_window_identity_for_target import SSMMaintenanceWindowIdentityForTarget


class SSMDescribeMaintenanceWindowsForTargetResponse(BaseModel):
    WindowIdentities: list[SSMMaintenanceWindowIdentityForTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

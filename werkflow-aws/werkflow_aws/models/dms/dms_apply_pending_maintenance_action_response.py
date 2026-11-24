from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_resource_pending_maintenance_actions import DMSResourcePendingMaintenanceActions


class DMSApplyPendingMaintenanceActionResponse(BaseModel):
    ResourcePendingMaintenanceActions: DMSResourcePendingMaintenanceActions | None = None
    ResponseMetadata: dict[str, Any] | None = None

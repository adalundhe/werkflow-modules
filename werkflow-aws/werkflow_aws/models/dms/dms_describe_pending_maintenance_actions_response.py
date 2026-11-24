from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_resource_pending_maintenance_actions import DMSResourcePendingMaintenanceActions


class DMSDescribePendingMaintenanceActionsResponse(BaseModel):
    PendingMaintenanceActions: list[DMSResourcePendingMaintenanceActions] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

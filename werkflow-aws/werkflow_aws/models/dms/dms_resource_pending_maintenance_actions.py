from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_pending_maintenance_action import DMSPendingMaintenanceAction


class DMSResourcePendingMaintenanceActions(BaseModel):
    ResourceIdentifier: StrictStr | None = None
    PendingMaintenanceActionDetails: list[DMSPendingMaintenanceAction] | None = None

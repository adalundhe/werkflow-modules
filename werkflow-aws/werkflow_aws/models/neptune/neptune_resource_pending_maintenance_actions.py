from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_pending_maintenance_action import NeptunePendingMaintenanceAction


class NeptuneResourcePendingMaintenanceActions(BaseModel):
    ResourceIdentifier: StrictStr | None = None
    PendingMaintenanceActionDetails: list[NeptunePendingMaintenanceAction] | None = None

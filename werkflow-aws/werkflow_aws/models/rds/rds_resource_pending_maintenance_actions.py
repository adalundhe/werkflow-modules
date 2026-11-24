from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_pending_maintenance_action import RDSPendingMaintenanceAction


class RDSResourcePendingMaintenanceActions(BaseModel):
    ResourceIdentifier: StrictStr | None = None
    PendingMaintenanceActionDetails: list[RDSPendingMaintenanceAction] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_resource_pending_maintenance_actions import RDSResourcePendingMaintenanceActions


class RDSDescribePendingMaintenanceActionsResponse(BaseModel):
    PendingMaintenanceActions: list[RDSResourcePendingMaintenanceActions] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

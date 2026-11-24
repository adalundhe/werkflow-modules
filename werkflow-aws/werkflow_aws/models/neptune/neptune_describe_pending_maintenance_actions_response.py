from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_resource_pending_maintenance_actions import NeptuneResourcePendingMaintenanceActions


class NeptuneDescribePendingMaintenanceActionsResponse(BaseModel):
    PendingMaintenanceActions: list[NeptuneResourcePendingMaintenanceActions] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

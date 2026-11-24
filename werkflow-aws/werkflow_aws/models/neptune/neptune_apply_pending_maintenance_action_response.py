from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_resource_pending_maintenance_actions import NeptuneResourcePendingMaintenanceActions


class NeptuneApplyPendingMaintenanceActionResponse(BaseModel):
    ResourcePendingMaintenanceActions: NeptuneResourcePendingMaintenanceActions | None = None
    ResponseMetadata: dict[str, Any] | None = None

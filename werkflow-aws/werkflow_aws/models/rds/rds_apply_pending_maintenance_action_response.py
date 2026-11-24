from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_resource_pending_maintenance_actions import RDSResourcePendingMaintenanceActions


class RDSApplyPendingMaintenanceActionResponse(BaseModel):
    ResourcePendingMaintenanceActions: RDSResourcePendingMaintenanceActions | None = None
    ResponseMetadata: dict[str, Any] | None = None

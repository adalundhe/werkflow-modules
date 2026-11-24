from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_resource_pending_maintenance_actions import DocumentDBResourcePendingMaintenanceActions


class DocumentDBDescribePendingMaintenanceActionsResponse(BaseModel):
    PendingMaintenanceActions: list[DocumentDBResourcePendingMaintenanceActions] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

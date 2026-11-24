from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_db_resource_pending_maintenance_actions import DocumentDBResourcePendingMaintenanceActions


class DocumentDBApplyPendingMaintenanceActionResponse(BaseModel):
    ResourcePendingMaintenanceActions: DocumentDBResourcePendingMaintenanceActions | None = None
    ResponseMetadata: dict[str, Any] | None = None

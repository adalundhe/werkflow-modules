from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_pending_maintenance_action import DocumentDBPendingMaintenanceAction


class DocumentDBResourcePendingMaintenanceActions(BaseModel):
    ResourceIdentifier: StrictStr | None = None
    PendingMaintenanceActionDetails: list[DocumentDBPendingMaintenanceAction] | None = None

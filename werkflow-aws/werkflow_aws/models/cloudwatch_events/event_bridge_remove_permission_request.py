from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EventBridgeRemovePermissionRequest(BaseModel):
    StatementId: StrictStr | None = None
    RemoveAllPermissions: StrictBool | None = None
    EventBusName: StrictStr | None = None

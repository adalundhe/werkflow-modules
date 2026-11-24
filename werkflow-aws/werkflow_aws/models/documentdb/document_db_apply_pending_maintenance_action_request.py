from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBApplyPendingMaintenanceActionRequest(BaseModel):
    ResourceIdentifier: StrictStr
    ApplyAction: StrictStr
    OptInType: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneApplyPendingMaintenanceActionRequest(BaseModel):
    ResourceIdentifier: StrictStr
    ApplyAction: StrictStr
    OptInType: StrictStr

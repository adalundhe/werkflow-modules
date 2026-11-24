from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSApplyPendingMaintenanceActionRequest(BaseModel):
    ReplicationInstanceArn: StrictStr
    ApplyAction: StrictStr
    OptInType: StrictStr

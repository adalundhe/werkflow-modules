from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteScheduledAuditRequest(BaseModel):
    scheduledAuditName: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeScheduledAuditRequest(BaseModel):
    scheduledAuditName: StrictStr

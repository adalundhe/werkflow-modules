from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTScheduledAuditMetadata(BaseModel):
    scheduledAuditName: StrictStr | None = None
    scheduledAuditArn: StrictStr | None = None
    frequency: StrictStr | None = None
    dayOfMonth: StrictStr | None = None
    dayOfWeek: StrictStr | None = None

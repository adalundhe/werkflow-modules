from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTDescribeScheduledAuditResponse(BaseModel):
    frequency: StrictStr | None = None
    dayOfMonth: StrictStr | None = None
    dayOfWeek: StrictStr | None = None
    targetCheckNames: list[StrictStr] | None = None
    scheduledAuditName: StrictStr | None = None
    scheduledAuditArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateScheduledAuditResponse(BaseModel):
    scheduledAuditArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

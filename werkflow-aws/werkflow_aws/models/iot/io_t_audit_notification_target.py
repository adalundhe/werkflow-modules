from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAuditNotificationTarget(BaseModel):
    targetArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    enabled: StrictBool | None = None

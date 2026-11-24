from __future__ import annotations
from pydantic import BaseModel, StrictBool


class IoTDeleteAccountAuditConfigurationRequest(BaseModel):
    deleteScheduledAudits: StrictBool | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDNSLogsConfigurationResult(BaseModel):
    Status: StrictStr | None = None

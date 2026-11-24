from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsGuardDutyDetectorDataSourcesDnsLogsDetails(BaseModel):
    Status: StrictStr | None = None

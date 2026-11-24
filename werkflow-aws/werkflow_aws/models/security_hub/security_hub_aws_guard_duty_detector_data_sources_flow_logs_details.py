from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsGuardDutyDetectorDataSourcesFlowLogsDetails(BaseModel):
    Status: StrictStr | None = None

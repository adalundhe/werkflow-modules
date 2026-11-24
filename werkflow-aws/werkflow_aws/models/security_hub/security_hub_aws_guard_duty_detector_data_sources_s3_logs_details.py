from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsGuardDutyDetectorDataSourcesS3LogsDetails(BaseModel):
    Status: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsGuardDutyDetectorDataSourcesCloudTrailDetails(BaseModel):
    Status: StrictStr | None = None

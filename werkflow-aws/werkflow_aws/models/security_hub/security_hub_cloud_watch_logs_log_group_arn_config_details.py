from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCloudWatchLogsLogGroupArnConfigDetails(BaseModel):
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
    Id: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53QueryLoggingConfig(BaseModel):
    Id: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
    CloudWatchLogsLogGroupArn: StrictStr | None = None

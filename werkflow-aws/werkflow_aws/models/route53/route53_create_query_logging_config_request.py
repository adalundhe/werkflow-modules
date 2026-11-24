from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CreateQueryLoggingConfigRequest(BaseModel):
    HostedZoneId: StrictStr
    CloudWatchLogsLogGroupArn: StrictStr

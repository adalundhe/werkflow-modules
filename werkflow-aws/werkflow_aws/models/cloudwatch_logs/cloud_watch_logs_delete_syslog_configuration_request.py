from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteSyslogConfigurationRequest(BaseModel):
    logGroupIdentifier: StrictStr
    vpcEndpointId: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutSyslogConfigurationRequest(BaseModel):
    logGroupIdentifier: StrictStr
    vpcEndpointId: StrictStr | None = None

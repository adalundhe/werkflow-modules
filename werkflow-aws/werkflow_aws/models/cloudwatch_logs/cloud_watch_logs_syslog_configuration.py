from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsSyslogConfiguration(BaseModel):
    logGroupArn: StrictStr | None = None
    sourceType: StrictStr | None = None
    vpcEndpointId: StrictStr | None = None
    createdAt: StrictInt | None = None

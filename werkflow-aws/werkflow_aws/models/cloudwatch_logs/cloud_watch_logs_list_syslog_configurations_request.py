from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsListSyslogConfigurationsRequest(BaseModel):
    logGroupIdentifier: StrictStr | None = None
    vpcEndpointId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

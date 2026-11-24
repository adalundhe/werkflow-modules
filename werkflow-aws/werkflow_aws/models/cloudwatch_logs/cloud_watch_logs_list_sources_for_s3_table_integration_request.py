from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsListSourcesForS3TableIntegrationRequest(BaseModel):
    integrationArn: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None

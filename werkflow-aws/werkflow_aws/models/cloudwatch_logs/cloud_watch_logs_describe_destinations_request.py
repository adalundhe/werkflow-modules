from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeDestinationsRequest(BaseModel):
    DestinationNamePrefix: StrictStr | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None

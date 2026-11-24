from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeDeliverySourcesRequest(BaseModel):
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    resourceArns: list[StrictStr] | None = None

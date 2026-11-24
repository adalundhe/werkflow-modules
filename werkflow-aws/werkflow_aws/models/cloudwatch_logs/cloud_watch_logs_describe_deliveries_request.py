from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeDeliveriesRequest(BaseModel):
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    deliverySourceNames: list[StrictStr] | None = None

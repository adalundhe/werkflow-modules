from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeDeliveryDestinationsRequest(BaseModel):
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    names: list[StrictStr] | None = None

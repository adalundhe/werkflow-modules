from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSDescribeGatewayResourcesRequest(BaseModel):
    gateway: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None

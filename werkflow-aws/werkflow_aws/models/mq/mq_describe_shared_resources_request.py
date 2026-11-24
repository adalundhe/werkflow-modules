from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MQDescribeSharedResourcesRequest(BaseModel):
    BrokerId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

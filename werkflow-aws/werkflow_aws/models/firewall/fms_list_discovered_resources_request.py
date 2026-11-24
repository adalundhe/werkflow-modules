from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSListDiscoveredResourcesRequest(BaseModel):
    MemberAccountIds: list[StrictStr]
    ResourceType: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

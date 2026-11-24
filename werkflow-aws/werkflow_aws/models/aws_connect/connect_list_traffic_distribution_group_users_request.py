from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListTrafficDistributionGroupUsersRequest(BaseModel):
    TrafficDistributionGroupId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

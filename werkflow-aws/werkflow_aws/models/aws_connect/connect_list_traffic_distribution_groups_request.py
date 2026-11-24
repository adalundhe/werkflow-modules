from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListTrafficDistributionGroupsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    InstanceId: StrictStr | None = None

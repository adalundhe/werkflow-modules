from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListRoutingProfileQueuesRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

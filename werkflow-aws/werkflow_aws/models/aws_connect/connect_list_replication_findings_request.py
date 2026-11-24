from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListReplicationFindingsRequest(BaseModel):
    InstanceId: StrictStr
    ResourceType: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

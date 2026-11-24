from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListContactFlowVersionsRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

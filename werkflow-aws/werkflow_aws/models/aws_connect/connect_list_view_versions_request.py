from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListViewVersionsRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

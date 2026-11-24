from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListInstancesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

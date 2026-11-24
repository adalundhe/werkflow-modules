from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListAuthenticationProfilesRequest(BaseModel):
    InstanceId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

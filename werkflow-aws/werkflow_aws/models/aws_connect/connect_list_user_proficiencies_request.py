from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListUserProficienciesRequest(BaseModel):
    InstanceId: StrictStr
    UserId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

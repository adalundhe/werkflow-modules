from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MQListUsersRequest(BaseModel):
    BrokerId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListAssociatedContactsRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

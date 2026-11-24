from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferListUsersRequest(BaseModel):
    ServerId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

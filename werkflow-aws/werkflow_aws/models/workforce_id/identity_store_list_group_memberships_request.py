from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IdentityStoreListGroupMembershipsRequest(BaseModel):
    IdentityStoreId: StrictStr
    GroupId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

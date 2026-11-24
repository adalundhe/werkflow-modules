from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDescribeGroupRequest(BaseModel):
    IdentityStoreId: StrictStr
    GroupId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDescribeUserRequest(BaseModel):
    IdentityStoreId: StrictStr
    UserId: StrictStr
    Extensions: list[StrictStr] | None = None

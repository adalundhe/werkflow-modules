from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDescribeIdentityStoreRequest(BaseModel):
    IdentityStoreId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDeleteGroupRequest(BaseModel):
    IdentityStoreId: StrictStr
    GroupId: StrictStr
    Revision: StrictStr | None = None

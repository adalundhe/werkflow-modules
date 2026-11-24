from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDeleteUserRequest(BaseModel):
    IdentityStoreId: StrictStr
    UserId: StrictStr
    Revision: StrictStr | None = None

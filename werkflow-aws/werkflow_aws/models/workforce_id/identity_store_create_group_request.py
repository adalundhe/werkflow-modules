from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreCreateGroupRequest(BaseModel):
    IdentityStoreId: StrictStr
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None

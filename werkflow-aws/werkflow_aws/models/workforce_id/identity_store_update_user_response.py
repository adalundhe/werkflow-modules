from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IdentityStoreUpdateUserResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    UserId: StrictStr | None = None
    UserArn: StrictStr | None = None
    Revision: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IdentityStoreGetUserIdResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    UserId: StrictStr | None = None
    UserArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

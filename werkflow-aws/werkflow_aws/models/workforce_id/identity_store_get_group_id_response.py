from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IdentityStoreGetGroupIdResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

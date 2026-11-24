from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IdentityStoreUpdateGroupResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupArn: StrictStr | None = None
    Revision: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

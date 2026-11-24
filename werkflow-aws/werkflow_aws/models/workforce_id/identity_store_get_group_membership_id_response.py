from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IdentityStoreGetGroupMembershipIdResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    MembershipId: StrictStr | None = None
    MembershipArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

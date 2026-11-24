from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListRoleMembershipsResponse(BaseModel):
    MembersList: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None

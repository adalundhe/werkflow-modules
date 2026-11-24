from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_group_member import QuickSightGroupMember


class QuickSightListGroupMembershipsResponse(BaseModel):
    GroupMemberList: list[QuickSightGroupMember] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None

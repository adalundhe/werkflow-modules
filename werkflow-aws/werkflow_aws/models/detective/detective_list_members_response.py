from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_member_detail import DetectiveMemberDetail


class DetectiveListMembersResponse(BaseModel):
    MemberDetails: list[DetectiveMemberDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

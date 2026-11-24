from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .detective_member_detail import DetectiveMemberDetail
from .detective_unprocessed_account import DetectiveUnprocessedAccount


class DetectiveGetMembersResponse(BaseModel):
    MemberDetails: list[DetectiveMemberDetail] | None = None
    UnprocessedAccounts: list[DetectiveUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_member_id_arn_pair import QuickSightMemberIdArnPair


class QuickSightListFolderMembersResponse(BaseModel):
    Status: StrictInt | None = None
    FolderMemberList: list[QuickSightMemberIdArnPair] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

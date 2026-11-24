from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_folder_member import QuickSightFolderMember


class QuickSightCreateFolderMembershipResponse(BaseModel):
    Status: StrictInt | None = None
    FolderMember: QuickSightFolderMember | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFolderMember(BaseModel):
    MemberId: StrictStr | None = None
    MemberType: StrictStr | None = None

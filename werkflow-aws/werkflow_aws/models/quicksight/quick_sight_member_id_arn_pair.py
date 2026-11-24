from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightMemberIdArnPair(BaseModel):
    MemberId: StrictStr | None = None
    MemberArn: StrictStr | None = None

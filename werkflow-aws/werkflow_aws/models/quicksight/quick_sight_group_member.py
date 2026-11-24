from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGroupMember(BaseModel):
    Arn: StrictStr | None = None
    MemberName: StrictStr | None = None

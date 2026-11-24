from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetLayoutGroupMember(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None

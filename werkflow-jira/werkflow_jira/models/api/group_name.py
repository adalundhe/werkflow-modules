from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GroupName(BaseModel):
    groupId: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueTypeInfo(BaseModel):
    avatarId: StrictInt | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None

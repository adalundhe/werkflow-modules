from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueTypeUpdateBean(BaseModel):
    avatarId: StrictInt | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None

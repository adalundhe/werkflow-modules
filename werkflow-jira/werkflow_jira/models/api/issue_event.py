from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueEvent(BaseModel):
    id: StrictInt | None = None
    name: StrictStr | None = None

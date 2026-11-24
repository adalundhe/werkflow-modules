from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeIds(BaseModel):
    issueTypeIds: list[StrictStr] | None = None

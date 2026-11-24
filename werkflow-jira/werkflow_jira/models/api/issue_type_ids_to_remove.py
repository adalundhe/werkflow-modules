from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeIdsToRemove(BaseModel):
    issueTypeIds: list[StrictStr] | None = None

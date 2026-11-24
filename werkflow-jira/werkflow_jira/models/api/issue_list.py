from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueList(BaseModel):
    issueIds: list[StrictStr] | None = None

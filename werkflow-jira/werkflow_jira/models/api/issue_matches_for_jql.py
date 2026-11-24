from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueMatchesForJQL(BaseModel):
    errors: list[StrictStr] | None = None
    matchedIssues: list[StrictInt] | None = None

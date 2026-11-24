from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BulkIssueIsWatching(BaseModel):
    issuesIsWatching: dict[StrictStr, StrictBool] | None = None

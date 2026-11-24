from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueBulkWatchOrUnwatchPayload(BaseModel):
    selectedIssueIdsOrKeys: list[StrictStr] | None = None

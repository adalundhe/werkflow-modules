from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueArchivalSyncRequest(BaseModel):
    issueIdsOrKeys: list[StrictStr] | None = None

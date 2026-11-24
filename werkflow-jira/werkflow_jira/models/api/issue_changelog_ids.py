from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IssueChangelogIds(BaseModel):
    changelogIds: list[StrictInt] | None = None

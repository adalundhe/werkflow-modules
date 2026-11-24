from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ProjectInsight(BaseModel):
    lastIssueUpdateTime: StrictStr | None = None
    totalIssueCount: StrictInt | None = None

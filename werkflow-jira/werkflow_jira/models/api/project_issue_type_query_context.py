from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectIssueTypeQueryContext(BaseModel):
    issueTypes: list[StrictStr] | None = None
    project: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectAndIssueTypePair(BaseModel):
    issueTypeId: StrictStr | None = None
    projectId: StrictStr | None = None

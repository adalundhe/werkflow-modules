from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ContextForProjectAndIssueType(BaseModel):
    contextId: StrictStr | None = None
    issueTypeId: StrictStr | None = None
    projectId: StrictStr | None = None

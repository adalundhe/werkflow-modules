from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowProjectIssueTypeUsage(BaseModel):
    id: StrictStr | None = None

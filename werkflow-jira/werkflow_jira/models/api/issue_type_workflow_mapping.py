from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IssueTypeWorkflowMapping(BaseModel):
    issueType: StrictStr | None = None
    updateDraftIfNeeded: StrictBool | None = None
    workflow: StrictStr | None = None

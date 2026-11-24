from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IssueTypesWorkflowMapping(BaseModel):
    defaultMapping: StrictBool | None = None
    issueTypes: list[StrictStr] | None = None
    updateDraftIfNeeded: StrictBool | None = None
    workflow: StrictStr | None = None

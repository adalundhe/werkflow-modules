from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .simplified_issue_transition import SimplifiedIssueTransition


class IssueBulkTransitionForWorkflow(BaseModel):
    isTransitionsFiltered: StrictBool | None = None
    issues: list[StrictStr] | None = None
    transitions: list[SimplifiedIssueTransition] | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .issue_transition_status import IssueTransitionStatus


class SimplifiedIssueTransition(BaseModel):
    to: IssueTransitionStatus | None = None
    transitionId: StrictInt | None = None
    transitionName: StrictStr | None = None

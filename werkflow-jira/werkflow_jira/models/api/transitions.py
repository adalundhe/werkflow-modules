from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_transition import IssueTransition


class Transitions(BaseModel):
    expand: StrictStr | None = None
    transitions: list[IssueTransition] | None = None

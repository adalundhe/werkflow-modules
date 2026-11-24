from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .suggested_issue import SuggestedIssue


class IssuePickerSuggestionsIssueType(BaseModel):
    id: StrictStr | None = None
    issues: list[SuggestedIssue] | None = None
    label: StrictStr | None = None
    msg: StrictStr | None = None
    sub: StrictStr | None = None

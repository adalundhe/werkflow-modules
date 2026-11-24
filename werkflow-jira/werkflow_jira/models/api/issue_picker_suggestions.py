from __future__ import annotations
from pydantic import BaseModel
from .issue_picker_suggestions_issue_type import IssuePickerSuggestionsIssueType


class IssuePickerSuggestions(BaseModel):
    sections: list[IssuePickerSuggestionsIssueType] | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_group_input import JiraGroupInput


class JiraMultipleGroupPickerField(BaseModel):
    fieldId: StrictStr | None = None
    groups: list[JiraGroupInput] | None = None

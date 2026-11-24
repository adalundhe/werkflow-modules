from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_user_field import JiraUserField


class JiraMultipleSelectUserPickerField(BaseModel):
    fieldId: StrictStr | None = None
    users: list[JiraUserField] | None = None

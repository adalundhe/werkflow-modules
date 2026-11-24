from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_user_field import JiraUserField


class JiraSingleSelectUserPickerField(BaseModel):
    fieldId: StrictStr | None = None
    user: JiraUserField | None = None

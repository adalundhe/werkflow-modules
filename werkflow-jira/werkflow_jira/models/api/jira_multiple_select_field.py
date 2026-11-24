from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_selected_option_field import JiraSelectedOptionField


class JiraMultipleSelectField(BaseModel):
    fieldId: StrictStr | None = None
    options: list[JiraSelectedOptionField] | None = None

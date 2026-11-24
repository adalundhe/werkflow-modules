from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_selected_option_field import JiraSelectedOptionField


class JiraSingleSelectField(BaseModel):
    fieldId: StrictStr | None = None
    option: JiraSelectedOptionField | None = None

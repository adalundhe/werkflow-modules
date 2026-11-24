from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_selected_option_field import JiraSelectedOptionField


class JiraCascadingSelectField(BaseModel):
    childOptionValue: JiraSelectedOptionField | None = None
    fieldId: StrictStr | None = None
    parentOptionValue: JiraSelectedOptionField | None = None

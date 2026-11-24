from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_color_input import JiraColorInput


class JiraColorField(BaseModel):
    color: JiraColorInput | None = None
    fieldId: StrictStr | None = None

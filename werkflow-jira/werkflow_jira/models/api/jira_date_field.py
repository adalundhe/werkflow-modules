from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_date_input import JiraDateInput


class JiraDateField(BaseModel):
    date: JiraDateInput | None = None
    fieldId: StrictStr | None = None

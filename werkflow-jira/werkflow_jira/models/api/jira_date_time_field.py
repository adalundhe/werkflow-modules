from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_date_time_input import JiraDateTimeInput


class JiraDateTimeField(BaseModel):
    dateTime: JiraDateTimeInput | None = None
    fieldId: StrictStr | None = None

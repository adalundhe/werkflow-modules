from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_version_field import JiraVersionField


class JiraSingleVersionPickerField(BaseModel):
    fieldId: StrictStr | None = None
    version: JiraVersionField | None = None

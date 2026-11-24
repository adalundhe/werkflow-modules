from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_version_field import JiraVersionField


class JiraMultipleVersionPickerField(BaseModel):
    bulkEditMultiSelectFieldOption: StrictStr | None = None
    fieldId: StrictStr | None = None
    versions: list[JiraVersionField] | None = None

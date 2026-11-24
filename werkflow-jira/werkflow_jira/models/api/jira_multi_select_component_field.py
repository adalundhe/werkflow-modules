from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_component_field import JiraComponentField


class JiraMultiSelectComponentField(BaseModel):
    bulkEditMultiSelectFieldOption: StrictStr | None = None
    components: list[JiraComponentField] | None = None
    fieldId: StrictStr | None = None

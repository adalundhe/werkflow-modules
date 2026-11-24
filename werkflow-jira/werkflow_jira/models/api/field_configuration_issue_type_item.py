from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldConfigurationIssueTypeItem(BaseModel):
    fieldConfigurationId: StrictStr | None = None
    fieldConfigurationSchemeId: StrictStr | None = None
    issueTypeId: StrictStr | None = None

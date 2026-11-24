from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldConfigurationToIssueTypeMapping(BaseModel):
    fieldConfigurationId: StrictStr | None = None
    issueTypeId: StrictStr | None = None

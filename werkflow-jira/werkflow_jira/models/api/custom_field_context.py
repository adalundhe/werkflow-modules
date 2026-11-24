from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldContext(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    isAnyIssueType: StrictBool | None = None
    isGlobalContext: StrictBool | None = None
    name: StrictStr | None = None

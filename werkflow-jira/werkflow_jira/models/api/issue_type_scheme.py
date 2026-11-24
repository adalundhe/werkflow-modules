from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IssueTypeScheme(BaseModel):
    defaultIssueTypeId: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    name: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeSchemeUpdateDetails(BaseModel):
    defaultIssueTypeId: StrictStr | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None

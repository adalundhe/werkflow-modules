from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeSchemeDetails(BaseModel):
    defaultIssueTypeId: StrictStr | None = None
    description: StrictStr | None = None
    issueTypeIds: list[StrictStr] | None = None
    name: StrictStr | None = None

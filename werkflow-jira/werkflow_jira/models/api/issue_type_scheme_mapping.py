from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeSchemeMapping(BaseModel):
    issueTypeId: StrictStr | None = None
    issueTypeSchemeId: StrictStr | None = None

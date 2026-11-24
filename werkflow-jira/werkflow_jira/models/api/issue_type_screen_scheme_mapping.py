from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeScreenSchemeMapping(BaseModel):
    issueTypeId: StrictStr | None = None
    screenSchemeId: StrictStr | None = None

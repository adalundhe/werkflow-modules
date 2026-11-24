from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeScreenSchemeItem(BaseModel):
    issueTypeId: StrictStr | None = None
    issueTypeScreenSchemeId: StrictStr | None = None
    screenSchemeId: StrictStr | None = None

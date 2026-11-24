from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeSchemeID(BaseModel):
    issueTypeSchemeId: StrictStr | None = None

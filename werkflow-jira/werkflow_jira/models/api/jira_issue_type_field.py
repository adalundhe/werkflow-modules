from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraIssueTypeField(BaseModel):
    issueTypeId: StrictStr | None = None

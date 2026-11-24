from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ArchiveIssueAsyncRequest(BaseModel):
    jql: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class JexpJqlIssues(BaseModel):
    maxResults: StrictInt | None = None
    query: StrictStr | None = None
    startAt: StrictInt | None = None
    validation: StrictStr | None = None

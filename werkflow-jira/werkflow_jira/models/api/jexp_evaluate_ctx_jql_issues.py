from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class JexpEvaluateCtxJqlIssues(BaseModel):
    maxResults: StrictInt | None = None
    nextPageToken: StrictStr | None = None
    query: StrictStr | None = None

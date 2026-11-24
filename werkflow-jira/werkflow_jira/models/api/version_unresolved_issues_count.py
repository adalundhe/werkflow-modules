from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class VersionUnresolvedIssuesCount(BaseModel):
    issuesCount: StrictInt | None = None
    issuesUnresolvedCount: StrictInt | None = None
    self: StrictStr | None = None

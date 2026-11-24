from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComponentIssuesCount(BaseModel):
    issueCount: StrictInt | None = None
    self: StrictStr | None = None

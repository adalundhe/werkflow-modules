from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusProjectIssueTypeUsage(BaseModel):
    id: StrictStr | None = None

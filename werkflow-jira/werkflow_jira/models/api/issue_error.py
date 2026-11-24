from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueError(BaseModel):
    errorMessage: StrictStr | None = None
    id: StrictStr | None = None

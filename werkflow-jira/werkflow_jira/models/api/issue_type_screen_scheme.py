from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeScreenScheme(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None

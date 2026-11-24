from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeScreenSchemeId(BaseModel):
    id: StrictStr | None = None

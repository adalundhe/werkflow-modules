from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeScreenSchemeUpdateDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None

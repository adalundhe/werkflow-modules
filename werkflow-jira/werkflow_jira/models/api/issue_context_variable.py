from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueContextVariable(BaseModel):
    id: StrictInt | None = None
    key: StrictStr | None = None
    type: StrictStr | None = None

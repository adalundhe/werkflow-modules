from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueTypeCreateBean(BaseModel):
    description: StrictStr | None = None
    hierarchyLevel: StrictInt | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None

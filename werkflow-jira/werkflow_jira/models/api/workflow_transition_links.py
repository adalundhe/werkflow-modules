from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkflowTransitionLinks(BaseModel):
    fromPort: StrictInt | None = None
    fromStatusReference: StrictStr | None = None
    toPort: StrictInt | None = None

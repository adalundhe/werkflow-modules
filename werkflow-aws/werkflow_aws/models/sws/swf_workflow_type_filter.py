from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFWorkflowTypeFilter(BaseModel):
    name: StrictStr
    version: StrictStr | None = None

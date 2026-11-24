from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WorkflowId(BaseModel):
    draft: StrictBool | None = None
    name: StrictStr | None = None

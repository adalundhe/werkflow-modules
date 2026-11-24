from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowSchemeIdName(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None

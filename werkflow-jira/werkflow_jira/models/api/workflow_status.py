from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WorkflowStatus(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    properties: dict[StrictStr, Any] | None = None

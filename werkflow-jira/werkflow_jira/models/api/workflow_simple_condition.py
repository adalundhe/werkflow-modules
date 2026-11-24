from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WorkflowSimpleCondition(BaseModel):
    configuration: dict[StrictStr, Any] | None = None
    nodeType: StrictStr | None = None
    type: StrictStr | None = None

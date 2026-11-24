from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WorkflowTransitionRule(BaseModel):
    configuration: Any = None
    type: StrictStr | None = None

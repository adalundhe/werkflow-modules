from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class WorkflowStatusLayout(BaseModel):
    x: StrictFloat | StrictInt | None = None
    y: StrictFloat | StrictInt | None = None

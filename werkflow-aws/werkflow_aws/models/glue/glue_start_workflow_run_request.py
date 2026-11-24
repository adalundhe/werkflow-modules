from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStartWorkflowRunRequest(BaseModel):
    Name: StrictStr
    RunProperties: dict[StrictStr, StrictStr] | None = None

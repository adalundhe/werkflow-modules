from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStopWorkflowRunRequest(BaseModel):
    Name: StrictStr
    RunId: StrictStr

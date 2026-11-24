from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueGetWorkflowRunRequest(BaseModel):
    Name: StrictStr
    RunId: StrictStr
    IncludeGraph: StrictBool | None = None

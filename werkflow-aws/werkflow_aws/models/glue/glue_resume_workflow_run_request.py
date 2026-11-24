from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueResumeWorkflowRunRequest(BaseModel):
    Name: StrictStr
    RunId: StrictStr
    NodeIds: list[StrictStr]

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetWorkflowRunRequest(BaseModel):
    spaceName: StrictStr
    id: StrictStr
    projectName: StrictStr

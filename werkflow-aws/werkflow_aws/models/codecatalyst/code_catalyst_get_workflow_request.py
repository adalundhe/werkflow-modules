from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetWorkflowRequest(BaseModel):
    spaceName: StrictStr
    id: StrictStr
    projectName: StrictStr

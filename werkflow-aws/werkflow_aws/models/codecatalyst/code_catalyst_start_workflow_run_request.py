from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystStartWorkflowRunRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    workflowId: StrictStr
    clientToken: StrictStr | None = None

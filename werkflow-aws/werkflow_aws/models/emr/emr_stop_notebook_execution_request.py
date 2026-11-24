from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRStopNotebookExecutionRequest(BaseModel):
    NotebookExecutionId: StrictStr

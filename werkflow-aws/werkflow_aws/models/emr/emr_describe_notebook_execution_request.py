from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRDescribeNotebookExecutionRequest(BaseModel):
    NotebookExecutionId: StrictStr

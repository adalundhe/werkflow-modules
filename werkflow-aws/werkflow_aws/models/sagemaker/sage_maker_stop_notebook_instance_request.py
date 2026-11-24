from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopNotebookInstanceRequest(BaseModel):
    NotebookInstanceName: StrictStr

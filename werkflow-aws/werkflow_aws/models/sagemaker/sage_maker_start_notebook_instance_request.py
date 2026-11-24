from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartNotebookInstanceRequest(BaseModel):
    NotebookInstanceName: StrictStr

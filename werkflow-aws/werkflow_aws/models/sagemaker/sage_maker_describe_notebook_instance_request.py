from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeNotebookInstanceRequest(BaseModel):
    NotebookInstanceName: StrictStr

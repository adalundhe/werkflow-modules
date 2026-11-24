from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeNotebookInstanceLifecycleConfigRequest(BaseModel):
    NotebookInstanceLifecycleConfigName: StrictStr

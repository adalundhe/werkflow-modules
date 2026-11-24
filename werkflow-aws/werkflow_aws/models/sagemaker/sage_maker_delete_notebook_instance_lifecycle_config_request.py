from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteNotebookInstanceLifecycleConfigRequest(BaseModel):
    NotebookInstanceLifecycleConfigName: StrictStr

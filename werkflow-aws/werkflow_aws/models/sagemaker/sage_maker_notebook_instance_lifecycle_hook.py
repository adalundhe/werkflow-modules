from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerNotebookInstanceLifecycleHook(BaseModel):
    Content: StrictStr | None = None

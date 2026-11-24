from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetNotebookMetadataRequest(BaseModel):
    NotebookId: StrictStr

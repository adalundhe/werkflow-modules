from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaExportNotebookRequest(BaseModel):
    NotebookId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaDeleteNotebookRequest(BaseModel):
    NotebookId: StrictStr

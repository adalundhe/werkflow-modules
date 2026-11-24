from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaCreatePresignedNotebookUrlRequest(BaseModel):
    SessionId: StrictStr

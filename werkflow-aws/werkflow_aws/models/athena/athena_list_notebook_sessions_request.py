from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaListNotebookSessionsRequest(BaseModel):
    NotebookId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

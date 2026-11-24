from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaUpdateNotebookMetadataRequest(BaseModel):
    NotebookId: StrictStr
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None

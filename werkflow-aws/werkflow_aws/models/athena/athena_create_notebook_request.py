from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaCreateNotebookRequest(BaseModel):
    WorkGroup: StrictStr
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None

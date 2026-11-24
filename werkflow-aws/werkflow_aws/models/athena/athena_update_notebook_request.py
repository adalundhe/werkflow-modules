from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AthenaUpdateNotebookRequest(BaseModel):
    NotebookId: StrictStr
    Payload: StrictStr
    Type: Literal['IPYNB']
    SessionId: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None

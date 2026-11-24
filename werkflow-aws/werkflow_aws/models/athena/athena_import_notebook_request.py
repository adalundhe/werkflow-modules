from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AthenaImportNotebookRequest(BaseModel):
    WorkGroup: StrictStr
    Name: StrictStr
    Type: Literal['IPYNB']
    Payload: StrictStr | None = None
    NotebookS3LocationUri: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None

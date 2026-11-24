from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneStartNotebookExportRequest(BaseModel):
    domainIdentifier: StrictStr
    notebookIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    fileFormat: Literal['PDF', 'IPYNB']
    clientToken: StrictStr | None = None

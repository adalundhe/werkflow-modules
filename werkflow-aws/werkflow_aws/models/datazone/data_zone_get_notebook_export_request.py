from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetNotebookExportRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr

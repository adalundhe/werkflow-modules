from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetNotebookRunRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr

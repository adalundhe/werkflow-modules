from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetNotebookRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteNotebookRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr

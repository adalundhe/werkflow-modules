from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneStopNotebookRunRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    clientToken: StrictStr | None = None

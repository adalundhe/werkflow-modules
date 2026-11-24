from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListNotebookRunsRequest(BaseModel):
    domainIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    notebookIdentifier: StrictStr | None = None
    status: Literal['QUEUED', 'STARTING', 'RUNNING', 'STOPPING', 'STOPPED', 'SUCCEEDED', 'FAILED'] | None = None
    scheduleIdentifier: StrictStr | None = None
    maxResults: StrictInt | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None

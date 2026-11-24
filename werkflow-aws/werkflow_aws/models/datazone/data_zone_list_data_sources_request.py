from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListDataSourcesRequest(BaseModel):
    domainIdentifier: StrictStr
    projectIdentifier: StrictStr
    environmentIdentifier: StrictStr | None = None
    connectionIdentifier: StrictStr | None = None
    type: StrictStr | None = None
    status: Literal['CREATING', 'FAILED_CREATION', 'READY', 'UPDATING', 'FAILED_UPDATE', 'RUNNING', 'DELETING', 'FAILED_DELETION'] | None = None
    name: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

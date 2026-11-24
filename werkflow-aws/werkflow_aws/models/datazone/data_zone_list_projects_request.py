from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListProjectsRequest(BaseModel):
    domainIdentifier: StrictStr
    userIdentifier: StrictStr | None = None
    groupIdentifier: StrictStr | None = None
    name: StrictStr | None = None
    projectCategory: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

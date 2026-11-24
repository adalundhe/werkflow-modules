from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListEnvironmentActionsRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

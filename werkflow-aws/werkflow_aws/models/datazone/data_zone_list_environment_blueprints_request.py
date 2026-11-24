from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DataZoneListEnvironmentBlueprintsRequest(BaseModel):
    domainIdentifier: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    name: StrictStr | None = None
    managed: StrictBool | None = None

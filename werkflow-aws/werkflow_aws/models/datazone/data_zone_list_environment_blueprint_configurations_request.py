from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListEnvironmentBlueprintConfigurationsRequest(BaseModel):
    domainIdentifier: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None

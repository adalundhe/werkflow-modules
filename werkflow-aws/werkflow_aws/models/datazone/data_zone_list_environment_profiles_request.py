from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListEnvironmentProfilesRequest(BaseModel):
    domainIdentifier: StrictStr
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
    environmentBlueprintIdentifier: StrictStr | None = None
    projectIdentifier: StrictStr | None = None
    name: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

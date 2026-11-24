from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneSearchGroupProfilesRequest(BaseModel):
    domainIdentifier: StrictStr
    groupType: Literal['SSO_GROUP', 'DATAZONE_SSO_GROUP', 'IAM_ROLE_SESSION_GROUP']
    searchText: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListEntityOwnersRequest(BaseModel):
    domainIdentifier: StrictStr
    entityType: Literal['DOMAIN_UNIT']
    entityIdentifier: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None

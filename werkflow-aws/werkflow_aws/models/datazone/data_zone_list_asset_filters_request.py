from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListAssetFiltersRequest(BaseModel):
    domainIdentifier: StrictStr
    assetIdentifier: StrictStr
    status: Literal['VALID', 'INVALID'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

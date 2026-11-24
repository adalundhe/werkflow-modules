from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetListingRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    listingRevision: StrictStr | None = None

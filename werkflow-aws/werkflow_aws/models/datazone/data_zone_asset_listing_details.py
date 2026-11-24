from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAssetListingDetails(BaseModel):
    listingId: StrictStr | None = None
    listingStatus: StrictStr | None = None

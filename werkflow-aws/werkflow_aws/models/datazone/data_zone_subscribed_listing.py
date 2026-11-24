from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_subscribed_listing_item import DataZoneSubscribedListingItem


class DataZoneSubscribedListing(BaseModel):
    id: StrictStr | None = None
    revision: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    item: DataZoneSubscribedListingItem | None = None
    ownerProjectId: StrictStr | None = None
    ownerProjectName: StrictStr | None = None

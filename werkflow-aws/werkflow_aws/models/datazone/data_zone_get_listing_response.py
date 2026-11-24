from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_listing_item import DataZoneListingItem


class DataZoneGetListingResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    listingRevision: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedBy: StrictStr | None = None
    item: DataZoneListingItem | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from pydantic import BaseModel
from .data_zone_listing_revision import DataZoneListingRevision


class DataZoneGrantedEntity(BaseModel):
    listing: DataZoneListingRevision | None = None

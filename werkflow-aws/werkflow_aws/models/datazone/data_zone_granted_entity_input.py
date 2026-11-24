from __future__ import annotations
from pydantic import BaseModel
from .data_zone_listing_revision_input import DataZoneListingRevisionInput


class DataZoneGrantedEntityInput(BaseModel):
    listing: DataZoneListingRevisionInput | None = None

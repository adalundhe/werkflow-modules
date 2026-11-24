from __future__ import annotations
from pydantic import BaseModel
from .data_zone_asset_listing import DataZoneAssetListing
from .data_zone_data_product_listing import DataZoneDataProductListing


class DataZoneListingItem(BaseModel):
    assetListing: DataZoneAssetListing | None = None
    dataProductListing: DataZoneDataProductListing | None = None

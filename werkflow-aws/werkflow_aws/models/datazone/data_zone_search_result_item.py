from __future__ import annotations
from pydantic import BaseModel
from .data_zone_asset_listing_item import DataZoneAssetListingItem
from .data_zone_data_product_listing_item import DataZoneDataProductListingItem


class DataZoneSearchResultItem(BaseModel):
    assetListing: DataZoneAssetListingItem | None = None
    dataProductListing: DataZoneDataProductListingItem | None = None

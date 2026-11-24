from __future__ import annotations
from pydantic import BaseModel
from .data_zone_subscribed_asset_listing import DataZoneSubscribedAssetListing
from .data_zone_subscribed_product_listing import DataZoneSubscribedProductListing


class DataZoneSubscribedListingItem(BaseModel):
    assetListing: DataZoneSubscribedAssetListing | None = None
    productListing: DataZoneSubscribedProductListing | None = None

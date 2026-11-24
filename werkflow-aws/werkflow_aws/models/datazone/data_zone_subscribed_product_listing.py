from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_asset_in_data_product_listing_item import DataZoneAssetInDataProductListingItem
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm


class DataZoneSubscribedProductListing(BaseModel):
    entityId: StrictStr | None = None
    entityRevision: StrictStr | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    assetListings: list[DataZoneAssetInDataProductListingItem] | None = None

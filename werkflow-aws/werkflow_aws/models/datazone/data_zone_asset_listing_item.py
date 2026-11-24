from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_asset_listing_item_additional_attributes import DataZoneAssetListingItemAdditionalAttributes
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm


class DataZoneAssetListingItem(BaseModel):
    listingId: StrictStr | None = None
    listingRevision: StrictStr | None = None
    name: StrictStr | None = None
    entityId: StrictStr | None = None
    entityRevision: StrictStr | None = None
    entityType: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    listingCreatedBy: StrictStr | None = None
    listingUpdatedBy: StrictStr | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    governedGlossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    owningProjectId: StrictStr | None = None
    additionalAttributes: DataZoneAssetListingItemAdditionalAttributes | None = None

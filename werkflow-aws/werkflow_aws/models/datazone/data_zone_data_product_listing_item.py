from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_data_product_listing_item_additional_attributes import DataZoneDataProductListingItemAdditionalAttributes
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm
from .data_zone_listing_summary_item import DataZoneListingSummaryItem


class DataZoneDataProductListingItem(BaseModel):
    listingId: StrictStr | None = None
    listingRevision: StrictStr | None = None
    name: StrictStr | None = None
    entityId: StrictStr | None = None
    entityRevision: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    listingCreatedBy: StrictStr | None = None
    listingUpdatedBy: StrictStr | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    owningProjectId: StrictStr | None = None
    additionalAttributes: DataZoneDataProductListingItemAdditionalAttributes | None = None
    items: list[DataZoneListingSummaryItem] | None = None

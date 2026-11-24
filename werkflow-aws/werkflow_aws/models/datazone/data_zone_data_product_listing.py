from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm
from .data_zone_listing_summary import DataZoneListingSummary


class DataZoneDataProductListing(BaseModel):
    dataProductId: StrictStr | None = None
    dataProductRevision: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    forms: StrictStr | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    owningProjectId: StrictStr | None = None
    items: list[DataZoneListingSummary] | None = None

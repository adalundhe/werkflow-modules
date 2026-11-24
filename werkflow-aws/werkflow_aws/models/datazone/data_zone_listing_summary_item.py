from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm


class DataZoneListingSummaryItem(BaseModel):
    listingId: StrictStr | None = None
    listingRevision: StrictStr | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None

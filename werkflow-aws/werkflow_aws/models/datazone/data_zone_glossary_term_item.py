from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_glossary_term_item_additional_attributes import DataZoneGlossaryTermItemAdditionalAttributes
from .data_zone_term_relations import DataZoneTermRelations


class DataZoneGlossaryTermItem(BaseModel):
    domainId: StrictStr | None = None
    glossaryId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    shortDescription: StrictStr | None = None
    usageRestrictions: list[StrictStr] | None = None
    longDescription: StrictStr | None = None
    termRelations: DataZoneTermRelations | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    additionalAttributes: DataZoneGlossaryTermItemAdditionalAttributes | None = None

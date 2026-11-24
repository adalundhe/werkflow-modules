from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_glossary_item_additional_attributes import DataZoneGlossaryItemAdditionalAttributes


class DataZoneGlossaryItem(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    usageRestrictions: list[StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    additionalAttributes: DataZoneGlossaryItemAdditionalAttributes | None = None

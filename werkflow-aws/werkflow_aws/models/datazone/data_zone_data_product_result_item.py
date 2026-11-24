from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_data_product_item_additional_attributes import DataZoneDataProductItemAdditionalAttributes


class DataZoneDataProductResultItem(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    description: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    firstRevisionCreatedAt: datetime.datetime | StrictStr | None = None
    firstRevisionCreatedBy: StrictStr | None = None
    additionalAttributes: DataZoneDataProductItemAdditionalAttributes | None = None

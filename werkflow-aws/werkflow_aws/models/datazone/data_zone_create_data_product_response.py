from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_data_product_item import DataZoneDataProductItem
from .data_zone_form_output import DataZoneFormOutput


class DataZoneCreateDataProductResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    revision: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    description: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    items: list[DataZoneDataProductItem] | None = None
    formsOutput: list[DataZoneFormOutput] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    firstRevisionCreatedAt: datetime.datetime | StrictStr | None = None
    firstRevisionCreatedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

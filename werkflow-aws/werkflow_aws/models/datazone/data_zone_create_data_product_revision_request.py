from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_data_product_item import DataZoneDataProductItem
from .data_zone_form_input import DataZoneFormInput


class DataZoneCreateDataProductRevisionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr
    description: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    items: list[DataZoneDataProductItem] | None = None
    formsInput: list[DataZoneFormInput] | None = None
    clientToken: StrictStr | None = None

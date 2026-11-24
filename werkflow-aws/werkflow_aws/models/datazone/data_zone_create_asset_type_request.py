from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_form_entry_input import DataZoneFormEntryInput


class DataZoneCreateAssetTypeRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    formsInput: dict[StrictStr, DataZoneFormEntryInput]
    owningProjectIdentifier: StrictStr
    description: StrictStr | None = None

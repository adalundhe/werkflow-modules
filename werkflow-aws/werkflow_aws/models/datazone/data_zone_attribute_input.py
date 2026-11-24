from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_form_input import DataZoneFormInput


class DataZoneAttributeInput(BaseModel):
    attributeIdentifier: StrictStr
    forms: list[DataZoneFormInput]

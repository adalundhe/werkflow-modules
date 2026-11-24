from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_form_output import DataZoneFormOutput


class DataZoneBatchGetAttributeOutput(BaseModel):
    attributeIdentifier: StrictStr | None = None
    forms: list[DataZoneFormOutput] | None = None

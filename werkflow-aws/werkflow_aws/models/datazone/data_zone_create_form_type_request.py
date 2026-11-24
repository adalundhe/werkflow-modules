from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_model import DataZoneModel


class DataZoneCreateFormTypeRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    model: DataZoneModel
    owningProjectIdentifier: StrictStr
    status: Literal['ENABLED', 'DISABLED'] | None = None
    description: StrictStr | None = None

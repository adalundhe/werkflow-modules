from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_source_location import DataZoneSourceLocation


class DataZoneStartNotebookImportRequest(BaseModel):
    domainIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    sourceLocation: DataZoneSourceLocation
    name: StrictStr
    description: StrictStr | None = None
    type: Literal['DATA', 'SQL'] | None = None
    clientToken: StrictStr | None = None

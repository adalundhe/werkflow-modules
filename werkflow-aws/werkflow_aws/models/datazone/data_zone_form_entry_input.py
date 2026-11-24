from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneFormEntryInput(BaseModel):
    typeIdentifier: StrictStr
    typeRevision: StrictStr
    required: StrictBool | None = None

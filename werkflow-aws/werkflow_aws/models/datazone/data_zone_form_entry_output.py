from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneFormEntryOutput(BaseModel):
    typeName: StrictStr | None = None
    typeRevision: StrictStr | None = None
    required: StrictBool | None = None

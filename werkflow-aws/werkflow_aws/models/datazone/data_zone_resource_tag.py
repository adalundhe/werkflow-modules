from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneResourceTag(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
    source: StrictStr | None = None

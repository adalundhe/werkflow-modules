from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetMapGlyphsRequest(BaseModel):
    MapName: StrictStr
    FontStack: StrictStr
    FontUnicodeRange: StrictStr
    Key: StrictStr | None = None

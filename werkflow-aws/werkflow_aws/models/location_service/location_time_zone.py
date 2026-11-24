from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationTimeZone(BaseModel):
    Name: StrictStr | None = None
    Offset: StrictInt | None = None

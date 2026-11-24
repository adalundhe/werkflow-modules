from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53Coordinates(BaseModel):
    Latitude: StrictStr | None = None
    Longitude: StrictStr | None = None

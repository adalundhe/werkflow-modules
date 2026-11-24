from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetMapTileRequest(BaseModel):
    MapName: StrictStr
    Z: StrictStr
    X: StrictStr
    Y: StrictStr
    Key: StrictStr | None = None

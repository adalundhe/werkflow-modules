from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetMapSpritesRequest(BaseModel):
    MapName: StrictStr
    FileName: StrictStr
    Key: StrictStr | None = None

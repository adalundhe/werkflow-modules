from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetPlaceRequest(BaseModel):
    IndexName: StrictStr
    PlaceId: StrictStr
    Language: StrictStr | None = None
    Key: StrictStr | None = None

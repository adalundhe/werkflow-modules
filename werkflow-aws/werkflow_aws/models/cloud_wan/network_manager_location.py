from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerLocation(BaseModel):
    Address: StrictStr | None = None
    Latitude: StrictStr | None = None
    Longitude: StrictStr | None = None

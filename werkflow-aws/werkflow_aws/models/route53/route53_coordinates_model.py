from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CoordinatesModel(BaseModel):
    Latitude: StrictStr | None = None
    Longitude: StrictStr | None = None

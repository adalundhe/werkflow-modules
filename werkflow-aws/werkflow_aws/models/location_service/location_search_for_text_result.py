from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .location_place import LocationPlace


class LocationSearchForTextResult(BaseModel):
    Place: LocationPlace | None = None
    Distance: StrictFloat | StrictInt | None = None
    Relevance: StrictFloat | StrictInt | None = None
    PlaceId: StrictStr | None = None

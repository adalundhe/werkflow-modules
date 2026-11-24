from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_place import LocationPlace


class LocationGetPlaceResponse(BaseModel):
    Place: LocationPlace | None = None
    ResponseMetadata: dict[str, Any] | None = None

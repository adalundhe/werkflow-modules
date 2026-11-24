from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_maps_response_entry import LocationListMapsResponseEntry


class LocationListMapsResponse(BaseModel):
    Entries: list[LocationListMapsResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

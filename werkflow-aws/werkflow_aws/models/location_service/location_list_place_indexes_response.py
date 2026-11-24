from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_place_indexes_response_entry import LocationListPlaceIndexesResponseEntry


class LocationListPlaceIndexesResponse(BaseModel):
    Entries: list[LocationListPlaceIndexesResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

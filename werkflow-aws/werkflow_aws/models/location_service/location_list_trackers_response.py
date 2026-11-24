from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_trackers_response_entry import LocationListTrackersResponseEntry


class LocationListTrackersResponse(BaseModel):
    Entries: list[LocationListTrackersResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

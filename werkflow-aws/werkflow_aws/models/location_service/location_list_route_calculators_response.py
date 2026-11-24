from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_route_calculators_response_entry import LocationListRouteCalculatorsResponseEntry


class LocationListRouteCalculatorsResponse(BaseModel):
    Entries: list[LocationListRouteCalculatorsResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

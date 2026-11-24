from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_calculate_route_summary import LocationCalculateRouteSummary
from .location_leg import LocationLeg


class LocationCalculateRouteResponse(BaseModel):
    Legs: list[LocationLeg] | None = None
    Summary: LocationCalculateRouteSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_search_for_position_result import LocationSearchForPositionResult
from .location_search_place_index_for_position_summary import LocationSearchPlaceIndexForPositionSummary


class LocationSearchPlaceIndexForPositionResponse(BaseModel):
    Summary: LocationSearchPlaceIndexForPositionSummary | None = None
    Results: list[LocationSearchForPositionResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_search_for_text_result import LocationSearchForTextResult
from .location_search_place_index_for_text_summary import LocationSearchPlaceIndexForTextSummary


class LocationSearchPlaceIndexForTextResponse(BaseModel):
    Summary: LocationSearchPlaceIndexForTextSummary | None = None
    Results: list[LocationSearchForTextResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_search_for_suggestions_result import LocationSearchForSuggestionsResult
from .location_search_place_index_for_suggestions_summary import LocationSearchPlaceIndexForSuggestionsSummary


class LocationSearchPlaceIndexForSuggestionsResponse(BaseModel):
    Summary: LocationSearchPlaceIndexForSuggestionsSummary | None = None
    Results: list[LocationSearchForSuggestionsResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None

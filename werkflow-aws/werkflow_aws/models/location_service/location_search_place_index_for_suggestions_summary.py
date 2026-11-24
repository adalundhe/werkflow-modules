from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LocationSearchPlaceIndexForSuggestionsSummary(BaseModel):
    Text: StrictStr | None = None
    BiasPosition: list[StrictFloat | StrictInt] | None = None
    FilterBBox: list[StrictFloat | StrictInt] | None = None
    FilterCountries: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    DataSource: StrictStr | None = None
    Language: StrictStr | None = None
    FilterCategories: list[StrictStr] | None = None

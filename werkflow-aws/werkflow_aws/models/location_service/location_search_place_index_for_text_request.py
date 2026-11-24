from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LocationSearchPlaceIndexForTextRequest(BaseModel):
    IndexName: StrictStr
    Text: StrictStr
    BiasPosition: list[StrictFloat | StrictInt] | None = None
    FilterBBox: list[StrictFloat | StrictInt] | None = None
    FilterCountries: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    Language: StrictStr | None = None
    FilterCategories: list[StrictStr] | None = None
    Key: StrictStr | None = None

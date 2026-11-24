from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationSearchForSuggestionsResult(BaseModel):
    Text: StrictStr | None = None
    PlaceId: StrictStr | None = None
    Categories: list[StrictStr] | None = None
    SupplementalCategories: list[StrictStr] | None = None

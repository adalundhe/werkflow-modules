from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LocationSearchPlaceIndexForPositionSummary(BaseModel):
    Position: list[StrictFloat | StrictInt] | None = None
    MaxResults: StrictInt | None = None
    DataSource: StrictStr | None = None
    Language: StrictStr | None = None

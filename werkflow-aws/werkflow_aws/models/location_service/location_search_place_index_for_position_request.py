from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LocationSearchPlaceIndexForPositionRequest(BaseModel):
    IndexName: StrictStr
    Position: list[StrictFloat | StrictInt]
    MaxResults: StrictInt | None = None
    Language: StrictStr | None = None
    Key: StrictStr | None = None

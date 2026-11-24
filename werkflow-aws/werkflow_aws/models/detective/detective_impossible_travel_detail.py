from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DetectiveImpossibleTravelDetail(BaseModel):
    StartingIpAddress: StrictStr | None = None
    EndingIpAddress: StrictStr | None = None
    StartingLocation: StrictStr | None = None
    EndingLocation: StrictStr | None = None
    HourlyTimeDelta: StrictInt | None = None

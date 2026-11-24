from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFMarkerRecordedEventAttributes(BaseModel):
    markerName: StrictStr | None = None
    details: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None

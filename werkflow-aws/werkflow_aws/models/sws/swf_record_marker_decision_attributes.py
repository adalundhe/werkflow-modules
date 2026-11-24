from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRecordMarkerDecisionAttributes(BaseModel):
    markerName: StrictStr
    details: StrictStr | None = None

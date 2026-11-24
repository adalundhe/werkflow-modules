from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointSegmentCondition(BaseModel):
    SegmentId: StrictStr | None = None

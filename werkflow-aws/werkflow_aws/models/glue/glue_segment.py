from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueSegment(BaseModel):
    SegmentNumber: StrictInt
    TotalSegments: StrictInt

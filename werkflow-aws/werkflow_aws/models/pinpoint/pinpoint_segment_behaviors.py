from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_recency_dimension import PinpointRecencyDimension


class PinpointSegmentBehaviors(BaseModel):
    Recency: PinpointRecencyDimension | None = None

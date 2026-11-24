from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_segment_group import PinpointSegmentGroup


class PinpointSegmentGroupList(BaseModel):
    Groups: list[PinpointSegmentGroup] | None = None
    Include: StrictStr | None = None

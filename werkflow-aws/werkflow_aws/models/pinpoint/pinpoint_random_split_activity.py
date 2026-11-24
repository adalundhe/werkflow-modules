from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_random_split_entry import PinpointRandomSplitEntry


class PinpointRandomSplitActivity(BaseModel):
    Branches: list[PinpointRandomSplitEntry] | None = None

from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_sliding_window import CloudWatchSlidingWindow
from .cloud_watch_wall_clock_window import CloudWatchWallClockWindow


class CloudWatchEvaluationWindow(BaseModel):
    WallClockWindow: CloudWatchWallClockWindow | None = None
    SlidingWindow: CloudWatchSlidingWindow | None = None

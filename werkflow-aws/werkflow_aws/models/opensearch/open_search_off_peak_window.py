from __future__ import annotations
from pydantic import BaseModel
from .open_search_window_start_time import OpenSearchWindowStartTime


class OpenSearchOffPeakWindow(BaseModel):
    WindowStartTime: OpenSearchWindowStartTime | None = None

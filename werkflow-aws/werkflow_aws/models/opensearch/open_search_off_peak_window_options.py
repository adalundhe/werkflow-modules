from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .open_search_off_peak_window import OpenSearchOffPeakWindow


class OpenSearchOffPeakWindowOptions(BaseModel):
    Enabled: StrictBool | None = None
    OffPeakWindow: OpenSearchOffPeakWindow | None = None

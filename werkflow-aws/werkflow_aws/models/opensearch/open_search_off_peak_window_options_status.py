from __future__ import annotations
from pydantic import BaseModel
from .open_search_off_peak_window_options import OpenSearchOffPeakWindowOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchOffPeakWindowOptionsStatus(BaseModel):
    Options: OpenSearchOffPeakWindowOptions | None = None
    Status: OpenSearchOptionStatus | None = None

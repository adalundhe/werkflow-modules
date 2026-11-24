from __future__ import annotations
from pydantic import BaseModel
from .open_search_auto_tune_options import OpenSearchAutoTuneOptions
from .open_search_auto_tune_status import OpenSearchAutoTuneStatus


class OpenSearchAutoTuneOptionsStatus(BaseModel):
    Options: OpenSearchAutoTuneOptions | None = None
    Status: OpenSearchAutoTuneStatus | None = None

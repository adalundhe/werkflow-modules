from __future__ import annotations
from pydantic import BaseModel
from .open_search_scheduled_auto_tune_details import OpenSearchScheduledAutoTuneDetails


class OpenSearchAutoTuneDetails(BaseModel):
    ScheduledAutoTuneDetails: OpenSearchScheduledAutoTuneDetails | None = None

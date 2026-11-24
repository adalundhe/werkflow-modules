from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_auto_tune_details import OpenSearchAutoTuneDetails


class OpenSearchAutoTune(BaseModel):
    AutoTuneType: StrictStr | None = None
    AutoTuneDetails: OpenSearchAutoTuneDetails | None = None
